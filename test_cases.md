# Test Cases for GitHub Login Page

## Test Case 1: Login Page Elements
**Description**: Verify that all elements on the login page are displayed correctly.
- **Steps**:
  1. Open the GitHub login page (`https://github.com/login`).
  2. Verify the presence of the following:
     - Username field.
     - Password field.
     - "Sign in" button.
- **Expected Result**: All elements should be visible.

## Test Case 2: API Response Validation
**Description**: Validate user details from the GitHub API.
- **Steps**:
  1. Send a GET request to `https://api.github.com/users/octocat`.
  2. Verify the `login` and `public_repos` fields in the response.
- **Expected Result**: Correct values should be returned in the response.
