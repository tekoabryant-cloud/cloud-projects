# AWS Secure Identity and Storage Provisioning

## Project Overview

This project demonstrates the secure provisioning of AWS identity and storage resources using Amazon S3 and AWS Identity and Access Management (IAM).

The goal of the project was to create a secure S3 storage environment, implement least-privilege access through IAM, create a Finance Analyst user and group, and validate that authorized and unauthorized access behaved as expected.

The project focused on security, access control, testing, and validation using AWS services.

---

# Project Objectives

The objectives of this project were to:

1. Create a secure Amazon S3 storage bucket.
2. Keep public access blocked.
3. Create a custom IAM policy using the principle of least privilege.
4. Create an IAM group named Finance-Analyst.
5. Create an IAM user and assign the user to the Finance-Analyst group.
6. Test authorized access to the S3 bucket.
7. Test unauthorized access to AWS resources.
8. Document the security controls and testing results.
9. Demonstrate practical experience with AWS IAM and S3.

---

# AWS Services Used

The following AWS services were used in this project:

- Amazon S3
- AWS IAM
- Amazon EC2
- AWS Management Console
- AWS CLI
- Python
- Boto3

---

# Project Architecture

The project used the following basic architecture:

User
   |
   v
IAM User
   |
   v
Finance-Analyst IAM Group
   |
   v
Custom IAM Policy
   |
   v
Amazon S3 Bucket
   |
   v
Secure Object Storage

Amazon EC2 was also used to validate access restrictions and demonstrate an unauthorized access scenario.

---

# Step 1: Create the S3 Bucket

An Amazon S3 bucket was created to provide secure cloud-based object storage.

The bucket was configured with security as a priority.

The following security settings were applied:

- Block all public access was enabled.
- The bucket was not configured for public access.
- Access was controlled through AWS IAM permissions.
- Objects were stored inside the private S3 bucket.

The bucket was used to store and retrieve files for testing.

### Evidence

The screenshot below shows the S3 bucket created for the project.

![S3 Bucket](screenshots%201/Img_7587.jpeg)

---

# Step 2: Configure S3 Security

The S3 bucket was configured to prevent unauthorized public access.

Amazon S3 Block Public Access was enabled.

This configuration prevents accidental exposure of stored objects to the public internet.

The project followed the security principle that access should be explicitly granted rather than allowing public access by default.

---

# Step 3: Create the Custom IAM Policy

A custom IAM policy was created to provide the Finance Analyst with only the permissions required for the project.

The policy followed the principle of least privilege.

The purpose of least privilege is to provide users with only the permissions necessary to perform their assigned tasks.

The policy was designed to allow controlled access to the project S3 resources while preventing unnecessary access to other AWS services and resources.

### Evidence

The screenshot below shows the custom IAM policy created for the project.

![IAM Policy](screenshots%201/Img_7598.jpg)

---

# Step 4: Create the Finance-Analyst IAM Group

An IAM group named:

Finance-Analyst

was created.

The custom IAM policy was attached to the group.

Using an IAM group makes permission management easier because policies can be assigned to the group rather than individually configuring every user.

The structure was:

Finance-Analyst Group
        |
        v
Custom IAM Policy
        |
        v
S3 Permissions

---

# Step 5: Create the IAM User

An IAM user was created for the Finance Analyst role.

The user was added to the:

Finance-Analyst

group.

By placing the user into the group, the user inherited the permissions assigned to the group.

This demonstrated how AWS IAM can be used to manage access based on roles and responsibilities.

---

# Step 6: Test S3 Access

After configuring the IAM permissions, S3 access was tested.

The authorized user was able to interact with the S3 bucket according to the permissions defined in the custom IAM policy.

Testing included working with files stored in the bucket.

The project successfully demonstrated file operations including:

- Uploading files
- Listing files
- Downloading files

Files were successfully uploaded and downloaded from the S3 bucket.

The S3 bucket contained test files including:

- test.txt
- Img

This confirmed that the configured permissions allowed the intended S3 operations.

---

# Security Approach

Security was a major component of this project.

The following security controls were implemented:

## 1. Block Public Access

S3 Block Public Access was enabled to prevent accidental public exposure of stored objects.

## 2. Least Privilege

IAM permissions were designed around the principle of least privilege.

The Finance Analyst was given only the permissions necessary to work with the required S3 resources.

## 3. IAM Groups

The Finance-Analyst group was used to centrally manage permissions.

This makes permission management more scalable and reduces the possibility of inconsistent permissions between users.

## 4. Separation of Access

IAM was used to separate authorized access from unauthorized access.

Users should only be able to access AWS resources that are necessary for their responsibilities.

## 5. Private Storage

The S3 bucket remained private rather than being configured for public access.

---

# Testing and Validation

Testing was performed to verify that the security configuration worked as intended.

The following areas were tested:

### S3 Bucket Access

The authorized IAM user was tested against the S3 bucket.

The user was able to perform the permitted file operations.

### File Upload

A test file was uploaded to the S3 bucket.

The upload completed successfully.

### File Listing

The contents of the S3 bucket were listed successfully.

The bucket displayed the test files stored within it.

### File Download

A file was downloaded from the S3 bucket successfully.

This confirmed that the configured permissions allowed the required S3 operations.

### Unauthorized Access

An unauthorized EC2 access attempt was also tested.

The access attempt resulted in an AccessDenied/UnauthorizedAccess error.

This demonstrated that AWS IAM permissions were preventing access to resources that were not authorized.

---

# EC2 Access Validation

Amazon EC2 was used to validate access restrictions.

An access attempt was made from the EC2 environment against a resource for which the associated identity did not have the required permissions.

AWS rejected the request.

The resulting access-denied response demonstrated that IAM was enforcing the configured permissions.

This was an important validation of the project's security controls.

The test confirmed that:

- Authorized actions were allowed.
- Unauthorized actions were denied.
- IAM policies were being enforced.
- The environment was not relying on unrestricted access.

### Evidence

The screenshot below shows the Access Denied result from the unauthorized access test.

![EC2 Access Denied](screenshots%201/Img_7588.jpeg)

---

# Test Results

| Test | Expected Result | Actual Result | Status |
|------|------------------|---------------|--------|
| S3 bucket creation | Bucket created successfully | Bucket created | PASS |
| Public access protection | Public access blocked | Public access blocked | PASS |
| IAM group creation | Finance-Analyst group created | Group created | PASS |
| IAM policy creation | Custom policy created | Policy created | PASS |
| IAM user creation | User created successfully | User created | PASS |
| User assigned to group | User receives group permissions | User assigned | PASS |
| S3 file upload | File uploads successfully | File uploaded | PASS |
| S3 file listing | Objects can be listed | Objects listed | PASS |
| S3 file download | File downloads successfully | File downloaded | PASS |
| Unauthorized EC2 access | Request denied | Access denied | PASS |

---

# Evidence

Screenshots were captured during the project to document the AWS configuration and testing process.

The evidence includes screenshots showing:

1. S3 bucket creation.
2. S3 security configuration.
3. Block Public Access settings.
4. IAM policy configuration.
5. Finance-Analyst IAM group.
6. IAM user configuration.
7. Successful S3 access.
8. Files stored in the S3 bucket.
9. Successful file upload/download testing.
10. EC2 unauthorized access attempt.
11. Access denied/UnauthorizedAccess response.

These screenshots provide visual evidence that the AWS resources were configured and tested successfully.

---

# Project Results

The project successfully demonstrated secure AWS identity and storage provisioning.

The following results were achieved:

- A private S3 bucket was successfully created.
- Public access was blocked.
- A custom IAM policy was created.
- A Finance-Analyst IAM group was created.
- An IAM user was created and assigned to the group.
- Authorized S3 operations were successfully tested.
- Files were successfully uploaded to S3.
- Files were successfully listed.
- Files were successfully downloaded.
- Unauthorized access was successfully denied.
- EC2 access restrictions were validated.

The project demonstrated how AWS IAM and S3 can be combined to create a controlled and secure cloud storage environment.

---

# What I Learned

This project provided hands-on experience with several important AWS and cloud security concepts.

## IAM

I learned how AWS IAM controls access to AWS resources using users, groups, and policies.

I also learned the importance of assigning permissions based on job responsibilities.

## Least Privilege

I learned that users should receive only the permissions they need to complete their tasks.

This reduces the potential impact of compromised credentials or accidental actions.

## Amazon S3

I gained practical experience creating and securing S3 buckets and working with objects.

I also learned how S3 permissions affect the ability to upload, list, and download objects.

## Access Control

I learned how AWS can allow authorized actions while denying unauthorized requests.

The AccessDenied result provided practical confirmation that IAM policies were being enforced.

## Troubleshooting

I also gained experience troubleshooting AWS permissions and configuration issues.

During the project, I had to identify and correct permission-related problems before successfully completing the S3 file operations.

This helped reinforce the importance of carefully reviewing IAM policies, users, groups, and permissions when troubleshooting AWS access issues.

## Cloud Security

The project reinforced the importance of securing cloud resources before using them in production.

Security controls such as Block Public Access and least-privilege IAM permissions help reduce the risk of accidental exposure and unauthorized access.

---

# Challenges Encountered

Several challenges were encountered during the project.

Some of the challenges involved:

- Configuring IAM permissions correctly.
- Understanding the relationship between users, groups, and policies.
- Troubleshooting AccessDenied errors.
- Validating permissions from different environments.
- Ensuring that S3 operations were permitted while unauthorized actions remained blocked.

These challenges provided practical troubleshooting experience and helped strengthen my understanding of AWS security.

---

# Troubleshooting Process

When an access error occurred, the configuration was reviewed systematically.

The troubleshooting process included checking:

1. IAM user configuration.
2. IAM group membership.
3. Attached IAM policies.
4. S3 bucket permissions.
5. Resource names.
6. Requested AWS actions.
7. Access-denied error messages.

After reviewing the configuration and correcting the necessary permissions, the S3 operations were successfully completed.

---

# Security Best Practices Demonstrated

The project demonstrated several AWS security best practices:

- Enable MFA for privileged AWS accounts.
- Avoid using the root account for everyday tasks.
- Use IAM users and groups for access management.
- Apply least-privilege permissions.
- Keep S3 Block Public Access enabled.
- Avoid unnecessary permissions.
- Test both authorized and unauthorized access.
- Monitor and review permissions regularly.
- Remove unused credentials and resources.
- Document cloud security configurations.

---

# Business Use Case

A financial organization could use a similar architecture to securely store financial documents, reports, spreadsheets, and other business information.

For example, a Finance Analyst may need permission to upload and retrieve financial reports from an S3 bucket.

Instead of giving the employee broad AWS permissions, the organization can create an IAM group with limited permissions specifically for the required S3 resources.

This approach reduces unnecessary access and helps protect sensitive business data.

---

# Skills Demonstrated

This project demonstrates hands-on experience with:

- AWS IAM
- Amazon S3
- Cloud security
- Identity and access management
- Least-privilege access
- Access control
- AWS troubleshooting
- Linux/EC2 environment testing
- AWS CLI
- Python
- Boto3
- Cloud storage
- Security validation
- Technical documentation

---

# Project Conclusion

The AWS Secure Identity and Storage Provisioning project successfully demonstrated how to create and secure cloud storage while controlling user access through AWS IAM.

The project implemented a private S3 bucket, blocked public access, created a custom IAM policy, established a Finance-Analyst group, created an IAM user, and tested both authorized and unauthorized access.

Successful file upload and download operations confirmed that the required permissions were working.

The unauthorized access test also confirmed that AWS IAM was preventing access outside the user's assigned permissions.

Overall, this project provided practical experience with AWS cloud security, identity management, access control, troubleshooting, and documentation.

It demonstrates the ability to configure AWS resources securely and validate that security controls operate as intended.

---

# Evidence Checklist

The following evidence should be included with the project:

- [ ] S3 bucket created
- [ ] S3 Block Public Access enabled
- [ ] Custom IAM policy created
- [ ] Finance-Analyst IAM group created
- [ ] IAM user created
- [ ] User added to Finance-Analyst group
- [ ] S3 file uploaded successfully
- [ ] S3 files listed successfully
- [ ] S3 file downloaded successfully
- [ ] EC2 access-denied test
- [ ] AccessDenied/UnauthorizedAccess error
- [ ] Final project results

---!

# Final Project Status

PROJECT STATUS: COMPLETED

The AWS Secure Identity and Storage Provisioning project was successfully completed and tested.

Authorized S3 operations were successful, while unauthorized access was denied as expected.

The project provides documented evidence of practical AWS IAM, S3, cloud security, access control, and troubleshooting experience.