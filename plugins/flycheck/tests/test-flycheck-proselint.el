(require 'flycheck-buttercup)
(require 'flycheck-ert)
(require 'flycheck-proselint)
(require 'markdown-mode)

(add-hook 'markdown-mode-hook #'flycheck-mode)
(add-hook 'text-mode-hook #'flycheck-mode)
(add-hook 'message-mode-hook #'flycheck-mode)
(eval-after-load 'flycheck
  '(add-hook 'flycheck-mode-hook #'flycheck-proselint-setup))

(describe "Language English"
    (describe "flycheck-proselint"
        (it "parses example proselint output"
            (let ((output "demo.md:11:5: dates_times.dates Apostrophes aren't needed for decades.
demo.md:13:17: dates_times.dates When specifying a date range, write 'from X to Y'.
demo.md:163:2: typography.symbols.copyright (c) is a goofy alphabetic approximation, use the symbol ©.
"))
              (with-temp-buffer
                (expect
                 (flycheck-parse-output output 'proselint (current-buffer))
                 :to-be-equal-flycheck-errors
                 (list
                  (flycheck-error-new-at
                   11 5 'warning
                   "Apostrophes aren't needed for decades."
                   :id "dates_times.dates"
                   :checker 'proselint
                   :buffer (current-buffer)
                   :filename "demo.md")
                  (flycheck-error-new-at
                   13 17 'warning
                   "When specifying a date range, write 'from X to Y'."
                   :id "dates_times.dates"
                   :checker 'proselint
                   :buffer (current-buffer)
                   :filename "demo.md")
                  (flycheck-error-new-at
                   163 2 'warning
                   "(c) is a goofy alphabetic approximation, use the symbol ©."
                   :id "typography.symbols.copyright"
                   :checker 'proselint
                   :buffer (current-buffer)
                   :filename "demo.md"))))))

        (it "activates in appropriate major modes"
            (expect (flycheck-ert-should-syntax-check
                     "tests/sample"
                     '(text-mode markdown-mode gfm-mode message-mode)
                     '(1 10 warning
                         "Inconsistent spelling of 'color' (vs. 'colour')."
                         :id "consistency.spelling"
                         :checker proselint)
                     '(2 16 warning
                         "With lowercase letters, the periods are standard."
                         :id "dates_times.am_pm.lowercase_periods"
                         :checker proselint))
                    :to-be nil))))
