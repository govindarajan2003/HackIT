django
djangorestframework
sudo apt-get install libmysqlclient-dev
sudo apt-get install pkg-config

pip install mysqlclient

The error message "Your password does not satisfy the current policy requirements" indicates that the MySQL server has a password policy in place, and the password you provided does not meet the requirements set by that policy.

MySQL password policies often include rules such as minimum length, requiring a mix of uppercase and lowercase letters, numbers, and special characters.

To resolve this issue, you can either choose a password that meets the policy requirements or adjust the password policy for the MySQL server. Here's an example of how to set a less strict password policy for the MySQL server:

1. Connect to MySQL as the root user:

   ```bash
   mysql -u root -p
   ```

2. Set the password policy to a more permissive mode:

   ```sql
   SET GLOBAL validate_password.policy = 0;
   ```

3. Create the user with the desired password:

   ```sql
   CREATE USER 'hackit_admin'@'localhost' IDENTIFIED BY 'root_admin123';
   ```

4. If needed, you can reset the password policy back to its original state:
   ```sql
   SET GLOBAL validate_password.policy = 1;
   ```

Please note that adjusting the password policy to be less strict may have security implications, so it's important to choose strong passwords even if the policy is relaxed.

If you prefer to set a more complex password that complies with the existing policy, you can choose a password that includes a mix of uppercase and lowercase letters, numbers, and special characters.

npm init -y

npm install express body-parser
