"""Health monitoring and diagnostics for proselint."""

from __future__ import annotations

import json
import platform
import psutil
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

from proselint import __version__
from proselint.logger import get_logger

logger = get_logger("monitoring")


@dataclass
class SystemHealth:
    """System health metrics."""
    timestamp: str
    cpu_percent: float
    memory_percent: float
    memory_available_mb: float
    disk_usage_percent: float
    python_version: str
    proselint_version: str
    platform: str
    uptime_seconds: float


@dataclass
class CheckHealth:
    """Health metrics for a specific check."""
    check_path: str
    execution_count: int
    success_count: int
    failure_count: int
    average_time_ms: float
    max_time_ms: float
    last_error: Optional[str]
    last_run: Optional[str]
    
    @property
    def success_rate(self) -> float:
        """Calculate success rate."""
        total = self.success_count + self.failure_count
        return (self.success_count / total * 100) if total > 0 else 100.0


@dataclass
class PerformanceMetrics:
    """Performance metrics."""
    files_processed: int
    total_errors_found: int
    total_processing_time: float
    cache_hit_rate: float
    average_file_size: float
    average_processing_speed: float  # bytes/second


class HealthMonitor:
    """Monitor system and application health."""
    
    def __init__(self, stats_file: Optional[Path] = None):
        """Initialize health monitor."""
        if stats_file is None:
            stats_file = Path.home() / '.proselint' / 'health.json'
        
        self.stats_file = stats_file
        self.stats_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.start_time = time.time()
        self.check_stats: Dict[str, CheckHealth] = {}
        self.performance = PerformanceMetrics(
            files_processed=0,
            total_errors_found=0,
            total_processing_time=0.0,
            cache_hit_rate=0.0,
            average_file_size=0.0,
            average_processing_speed=0.0
        )
        
        self._load_stats()
    
    def _load_stats(self) -> None:
        """Load statistics from file."""
        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r') as f:
                    data = json.load(f)
                    
                    # Load check stats
                    for check_path, stats in data.get('checks', {}).items():
                        self.check_stats[check_path] = CheckHealth(**stats)
                    
                    # Load performance metrics
                    if 'performance' in data:
                        self.performance = PerformanceMetrics(**data['performance'])
                        
            except Exception as e:
                logger.warning(f"Failed to load health stats: {e}")
    
    def _save_stats(self) -> None:
        """Save statistics to file."""
        try:
            data = {
                'version': __version__,
                'updated': datetime.now().isoformat(),
                'checks': {
                    path: asdict(health)
                    for path, health in self.check_stats.items()
                },
                'performance': asdict(self.performance)
            }
            
            with open(self.stats_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            logger.warning(f"Failed to save health stats: {e}")
    
    def get_system_health(self) -> SystemHealth:
        """Get current system health metrics."""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            return SystemHealth(
                timestamp=datetime.now().isoformat(),
                cpu_percent=cpu_percent,
                memory_percent=memory.percent,
                memory_available_mb=memory.available / (1024 * 1024),
                disk_usage_percent=disk.percent,
                python_version=sys.version.split()[0],
                proselint_version=__version__,
                platform=platform.platform(),
                uptime_seconds=time.time() - self.start_time
            )
        except Exception as e:
            logger.error(f"Failed to get system health: {e}")
            # Return default values on error
            return SystemHealth(
                timestamp=datetime.now().isoformat(),
                cpu_percent=0.0,
                memory_percent=0.0,
                memory_available_mb=0.0,
                disk_usage_percent=0.0,
                python_version=sys.version.split()[0],
                proselint_version=__version__,
                platform=platform.platform(),
                uptime_seconds=time.time() - self.start_time
            )
    
    def record_check_execution(
        self,
        check_path: str,
        success: bool,
        execution_time: float,
        error: Optional[str] = None
    ) -> None:
        """Record check execution metrics."""
        if check_path not in self.check_stats:
            self.check_stats[check_path] = CheckHealth(
                check_path=check_path,
                execution_count=0,
                success_count=0,
                failure_count=0,
                average_time_ms=0.0,
                max_time_ms=0.0,
                last_error=None,
                last_run=None
            )
        
        stats = self.check_stats[check_path]
        stats.execution_count += 1
        stats.last_run = datetime.now().isoformat()
        
        if success:
            stats.success_count += 1
        else:
            stats.failure_count += 1
            stats.last_error = error
        
        # Update timing metrics
        time_ms = execution_time * 1000
        
        # Calculate new average
        old_avg = stats.average_time_ms
        stats.average_time_ms = (
            (old_avg * (stats.execution_count - 1) + time_ms) /
            stats.execution_count
        )
        
        # Update max time
        stats.max_time_ms = max(stats.max_time_ms, time_ms)
    
    def record_file_processing(
        self,
        file_size: int,
        errors_found: int,
        processing_time: float,
        cache_hit: bool = False
    ) -> None:
        """Record file processing metrics."""
        self.performance.files_processed += 1
        self.performance.total_errors_found += errors_found
        self.performance.total_processing_time += processing_time
        
        # Update averages
        n = self.performance.files_processed
        
        # Update average file size
        old_avg_size = self.performance.average_file_size
        self.performance.average_file_size = (
            (old_avg_size * (n - 1) + file_size) / n
        )
        
        # Update average processing speed
        if processing_time > 0:
            speed = file_size / processing_time
            old_avg_speed = self.performance.average_processing_speed
            self.performance.average_processing_speed = (
                (old_avg_speed * (n - 1) + speed) / n
            )
        
        # Update cache hit rate
        if cache_hit:
            old_rate = self.performance.cache_hit_rate
            self.performance.cache_hit_rate = (
                (old_rate * (n - 1) + 100) / n
            )
        else:
            old_rate = self.performance.cache_hit_rate
            self.performance.cache_hit_rate = (
                (old_rate * (n - 1)) / n
            )
    
    def get_diagnostics(self) -> Dict[str, Any]:
        """Get comprehensive diagnostics."""
        system_health = self.get_system_health()
        
        # Find problematic checks
        problematic_checks = [
            stats for stats in self.check_stats.values()
            if stats.failure_count > stats.success_count or
               stats.average_time_ms > 1000
        ]
        
        # Calculate overall health score (0-100)
        health_score = 100
        
        # Deduct points for system issues
        if system_health.cpu_percent > 80:
            health_score -= 10
        if system_health.memory_percent > 80:
            health_score -= 10
        if system_health.disk_usage_percent > 90:
            health_score -= 15
        
        # Deduct points for check failures
        total_checks = len(self.check_stats)
        if total_checks > 0:
            avg_success_rate = sum(
                s.success_rate for s in self.check_stats.values()
            ) / total_checks
            
            if avg_success_rate < 90:
                health_score -= int((90 - avg_success_rate) / 2)
        
        # Deduct points for slow performance
        if self.performance.average_processing_speed > 0:
            if self.performance.average_processing_speed < 10000:  # < 10KB/s
                health_score -= 20
            elif self.performance.average_processing_speed < 50000:  # < 50KB/s
                health_score -= 10
        
        health_score = max(0, health_score)
        
        return {
            'health_score': health_score,
            'status': self._get_status(health_score),
            'system': asdict(system_health),
            'performance': asdict(self.performance),
            'problematic_checks': [
                asdict(check) for check in problematic_checks
            ],
            'recommendations': self._get_recommendations(
                health_score, system_health, problematic_checks
            )
        }
    
    def _get_status(self, score: int) -> str:
        """Get status from health score."""
        if score >= 90:
            return "healthy"
        elif score >= 70:
            return "degraded"
        elif score >= 50:
            return "unhealthy"
        else:
            return "critical"
    
    def _get_recommendations(
        self,
        health_score: int,
        system_health: SystemHealth,
        problematic_checks: List[CheckHealth]
    ) -> List[str]:
        """Get recommendations based on diagnostics."""
        recommendations = []
        
        if system_health.cpu_percent > 80:
            recommendations.append(
                "High CPU usage detected. Consider reducing parallel workers."
            )
        
        if system_health.memory_percent > 80:
            recommendations.append(
                "High memory usage. Consider processing smaller files or "
                "reducing cache size."
            )
        
        if system_health.disk_usage_percent > 90:
            recommendations.append(
                "Low disk space. Clear cache with --clear-cache."
            )
        
        if problematic_checks:
            check_names = [c.check_path for c in problematic_checks[:3]]
            recommendations.append(
                f"Disable problematic checks: {', '.join(check_names)}"
            )
        
        if self.performance.cache_hit_rate < 50:
            recommendations.append(
                "Low cache hit rate. Ensure caching is enabled."
            )
        
        if self.performance.average_processing_speed < 50000:
            recommendations.append(
                "Slow processing speed. Use --mode fast for better performance."
            )
        
        return recommendations
    
    def save(self) -> None:
        """Save current statistics."""
        self._save_stats()
    
    def reset(self) -> None:
        """Reset all statistics."""
        self.check_stats.clear()
        self.performance = PerformanceMetrics(
            files_processed=0,
            total_errors_found=0,
            total_processing_time=0.0,
            cache_hit_rate=0.0,
            average_file_size=0.0,
            average_processing_speed=0.0
        )
        self._save_stats()


# Global health monitor instance
_health_monitor: Optional[HealthMonitor] = None


def get_health_monitor() -> HealthMonitor:
    """Get global health monitor instance."""
    global _health_monitor
    if _health_monitor is None:
        _health_monitor = HealthMonitor()
    return _health_monitor