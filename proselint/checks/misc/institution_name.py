# -*- coding: utf-8 -*-

"""Common errors with institution names"""

from proselint.tools import memoize, preferred_forms_check



@memoize
def check_vtech(text):
    """Suggest the correct name.

    source: Virginia Tech Division of Student Affairs
    source_url: http://career.vt.edu/job-search/presenting_yourself/resumes/common-resume-mistakes.html
    """
    err = "institution.vtech"
    msg = "Incorrect name. Use '{}' instead of '{}'."

    institution = [
        ["Virginia Polytechnic Institute and State University",          ["Virginia Polytechnic and State University"]],
    ]
    return preferred_forms_check(text, institution, err, msg)
