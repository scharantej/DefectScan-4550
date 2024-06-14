## Python Flask Application Design

### HTML Files

#### 1. **index.html**
- Main HTML page.
- Displays the form for comment input and a button to submit it.
- The form should include two fields: `comment` (for comment text) and `system` (for selecting the bug tracking system from which the comment originated).

#### 2. **report.html**
- HTML page that displays the updated report.
- Includes a table to list the comments and their associated bug tracking systems.

### Routes

#### 1. **@app.route('/submit', methods=['POST'])**
- Receives the submitted comment form data.
- Extracts the comment text and bug tracking system from the form.
- Saves the comment and system information to a database or other data store.
- Redirects to the `/report` route.

#### 2. **@app.route('/report')**
- Queries the database or data store for all saved comments.
- Generates an HTML report with a table listing the comments and their bug tracking system.
- Renders the `report.html` page with the generated report.