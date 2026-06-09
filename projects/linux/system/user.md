# User Management

Effective user management is a fundamental aspect of Linux system administration. Administrators frequently need to create new user accounts or assign existing users to specific groups to enforce appropriate access controls.

To perform tasks that require elevated privileges, users can utilize the sudo command. The sudo command, short for "superuser do," allows permitted users to execute commands with the security privileges of another user, typically the superuser or root. This enables users to perform administrative tasks without logging in as the root user, which is a best practice for maintaining system security. We will explore sudo permissions in greater detail in the Linux Security section.

| Command | Description |
| --- | --- |
| sudo | Execute command as a different user. |
| su | The su utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser). A shell is then executed. |
| useradd | Creates a new user or update default new user information. |
| userdel | Deletes a user account and related files. |
| usermod | Modifies a user account. |
| addgroup | Adds a group to the system. |
| delgroup | Removes a group from the system. |
| passwd | Changes user password. |
