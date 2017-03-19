;;; flycheck-proselint.el --- A flycheck linter for prose

;; Version: 0.8.0
;; Package-Requires: ((flycheck "1"))
;; Keywords: languages, convenience
;; URL: http://proselint.com/

;;; Commentary:

;; The goal of proselint is to aggregate knowledge about best practices
;; in writing and to make that knowledge immediately accessible to all
;; authors in the form of a linter for prose.
;;
;; This package provides a proselint checker for flycheck.

;;; Usage:

;; (eval-after-load 'flycheck
;;   '(add-hook 'flycheck-mode-hook #'flycheck-proselint-setup))
;; (add-hook 'text-mode-hook #'flycheck-mode)
;; (add-hook 'markdown-mode-hook #'flycheck-mode)
;; (add-hook 'message-mode-hook #'flycheck-mode)
;; ...

;;; Code:

(require 'flycheck)

(flycheck-define-checker proselint
  "A linter for prose."
  :command ("proselint" source-inplace)
  :error-patterns
  ((warning line-start (file-name) ":" line ":" column ": "
            (id (one-or-more (not (any " "))))
            " "
            (message (one-or-more not-newline)
                     (zero-or-more "\n" (any " ") (one-or-more not-newline)))
            line-end))
  :modes (text-mode markdown-mode gfm-mode message-mode))

;;;###autoload
(defun flycheck-proselint-setup ()
  "Add proselist to list of flycheck checkers."
  (add-to-list 'flycheck-checkers 'proselint))

(provide 'flycheck-proselint)

;;; flycheck-proselint.el ends here
