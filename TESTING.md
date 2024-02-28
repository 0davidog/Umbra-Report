# Umbra Report Project Test File
## Contents
## Manual Testing
## Compatibility and Responsive Testing
## Accessibility Testing
### Accessibility Audits
### Keyboard Navigation
### Chrome Vox Reader
## Core Web Vitals

## Validation Testing

### CSS Validation

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code through direct input.

|Result|Screen Capture|
|------|--------------|
|No Error Found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/b962aa9c-223b-4f2d-8c4d-6629ff71bd91)|

### HTML Validation

[W3C  Markup Validation Service](https://validator.w3.org/) was used to validate the html through direct code input. The html was acquired for each page by viewing the page source code on the deployed site.

|Page|Result|Screen Capture|
|----|------|--------------|
|[Index](https://umbra-report-f975c52ec09c.herokuapp.com/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/3a002a03-5be4-4678-b8e2-b7f30cbef0eb)|
|[About](https://umbra-report-f975c52ec09c.herokuapp.com/about/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/01018cc3-95ac-4d3e-ae6f-87b969c6fffd)|
|[User01](https://umbra-report-f975c52ec09c.herokuapp.com/profile/0davidog/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/58d33ad5-f7e9-41fb-8c76-ccd935281961)|
|[User02](https://umbra-report-f975c52ec09c.herokuapp.com/profile/Nosferatu302/)| No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/a568860f-54e9-42d5-8e9a-9001befcb995)|
|[Report01](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/7bc1a4a2-56c9-4cb2-9111-be32d7df7eaa)|
|[Report02](https://umbra-report-f975c52ec09c.herokuapp.com/bermuda3/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/394e67e2-e07f-43c1-a20e-834d95bd7856)|
|[CreateReport](https://umbra-report-f975c52ec09c.herokuapp.com/create/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/62c24ec0-bd04-4917-a23b-1f27ef331e23)|
|[EditReport](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/edit/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/1386e7b6-731e-4b5d-a50a-f7ad6dcd014e)|
|[SignUp](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/signup/)|4 errors. * |[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/28ab4d89-9646-4853-b006-7c74e2ef400e)|
|[Login](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/login/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/ac4b0230-3554-4d5d-8b4f-e6ff24dcc90d)|
|[Logout](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/logout/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/bb469d00-1ce3-4f47-8722-80269e868760)|
|[404](https://umbra-report-f975c52ec09c.herokuapp.com/404/)| No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/a5598dab-1566-4ea2-97ea-94d353f2249e)|

* The 4 errors listed on the sign up page come from external html code that I don't have access to, so they are ignored for the time being.

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the two javascript files through direct input of code.

|File|Result|Screen Capture|
|----|------|--------------|
|comment.js|No error found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/edb12d97-8985-4962-a125-54fdbe050cbc)|
|delete_report.js|No error found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/46025848-c55d-47df-af60-0d7b22d99d04)|

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the relevant python files through direct input of code.

|File|Result|Screen Capture|
|----|------|--------------|
|umbra/urls.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/fae49a9e-873e-4831-98f9-abe2dc17a7cf)|
|blog/admin.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/4ef16586-cfd7-4029-8dc3-58ed3051f1b4)|
|blog/forms.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/f6ead999-65bd-467f-9bfe-652605c24271)|
|blog/models.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/8ea7317d-a3b4-407d-82a7-f79e7125ef77)|
|blog/urls.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/4c70200d-de4b-4296-b93d-ad36872cfd58)|
|blog/views.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/a2543ba0-da00-4fc9-a5af-9bbbf94ceb88)|

## Automated Testing
## Defects
## Defects of Note
## Outstanding Defects
