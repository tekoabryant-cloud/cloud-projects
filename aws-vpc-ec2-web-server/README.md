# AWS VPC Secure Web Server

## Project Overview

Built and deployed a publicly accessible web server in AWS using Amazon VPC and Amazon EC2.

This project demonstrates foundational AWS networking, compute, security, and web server configuration.

I created a custom VPC with a public subnet, Internet Gateway, route table, and security group. I then launched an EC2 instance inside the public subnet and configured Apache HTTP Server using EC2 User Data.

The completed web server successfully displayed:

> Welcome to My Cloud Portfolio Web Server
## Architecture

The web server architecture consists of:

Internet
   |
Internet Gateway
   |
VPC
   |
Public Subnet
   |
Route Table
   |
Security Group
   |
EC2 Web Server
   |
Apache HTTP Server
   |
Web Page
## AWS Services Used

- Amazon VPC — Created the isolated networking environment.
- Amazon EC2 — Hosted the web server.
- Amazon VPC Subnet — Provided the public network segment for the EC2 instance.
- Internet Gateway — Provided internet connectivity to the VPC.
- Route Table — Routed internet-bound traffic through the Internet Gateway.
- Security Group — Controlled inbound and outbound traffic to the EC2 instance.
## VPC Configuration

- VPC Name: cloud-portfolio-vpc
- IPv4 CIDR Block: 10.0.0.0/16

The VPC provides an isolated networking environment for the EC2 web server.
## Public Subnet Configuration

- Subnet Name: cloud-portfolio-public-subnet
- IPv4 CIDR Block: 10.0.1.0/24
- Availability Zone: us-east-1a

The public subnet was created inside the VPC to host the EC2 web server.

The subnet uses a route table with a route to the Internet Gateway, allowing internet-bound traffic.
## Internet Gateway Configuration

- Internet Gateway Name: cloud-portfolio-igw
- Attached VPC: cloud-portfolio-vpc

The Internet Gateway provides connectivity between the VPC and the internet.

It was attached to the VPC and configured as the target for the public subnet's internet route.
## Route Table Configuration

- Route Table Name: cloud-portfolio-public-rt
- Associated Subnet: cloud-portfolio-public-subnet

The route table was configured with:

- Destination: 0.0.0.0/0
- Target: Internet Gateway (cloud-portfolio-igw)

The 0.0.0.0/0 route directs internet-bound traffic through the Internet Gateway.
## Security Group Configuration

- Security Group Name: cloud-portfolio-web-sg
- Inbound Rule: HTTP (TCP port 80)
- Source: 0.0.0.0/0
- Outbound: Default outbound access

HTTP traffic was allowed from the internet because the web server was designed to be publicly accessible.

SSH access on port 22 was not opened to the entire internet. This follows the principle of least privilege because SSH provides administrative access and should be restricted to trusted sources.

The security group acts as a virtual firewall controlling network traffic to the EC2 instance.
## EC2 Instance Configuration

- Instance Name: cloud-portfolio-web-server
- AMI: Amazon Linux 2023
- Instance Type: t3.micro
- VPC: cloud-portfolio-vpc
- Subnet: cloud-portfolio-public-subnet
- Public IP: Enabled
- Security Group: cloud-portfolio-web-sg

The EC2 instance was launched inside the public subnet and assigned a public IP address so the web server could be accessed from the internet.
## Apache Web Server Configuration

Apache HTTP Server was installed and configured using EC2 User Data.

The User Data script automatically:

1. Updated the system packages.
2. Installed Apache.
3. Enabled the Apache service.
4. Started the Apache service.
5. Created an index.html webpage.

The completed webpage displayed:

> Welcome to My Cloud Portfolio Web Server
## EC2 User Data

EC2 User Data was used to automate the initial web server configuration.

The User Data script:

- Updated the system packages.
- Installed Apache.
- Enabled the Apache service.
- Started the Apache service.
- Created the website's `index.html` file.

Using User Data reduced the need for manual configuration after launching the EC2 instance and allowed the web server to be configured automatically at startup.
## Testing and Validation

After launching the EC2 instance, I verified that:

- The EC2 instance was running.
- A public IP address was assigned.
- The correct security group was attached.
- HTTP traffic was allowed on port 80.
- The subnet was associated with the correct route table.
- The route table contained a `0.0.0.0/0` route to the Internet Gateway.
- The Internet Gateway was attached to the VPC.
- The Apache web server was running.

I successfully accessed the web server through the EC2 instance's public IP address and verified that the webpage displayed:

> Welcome to My Cloud Portfolio Web Server
## Security Considerations

Security was considered throughout the project using the principle of least privilege.

- HTTP traffic on port 80 was allowed because the web server was intended to be publicly accessible.
- SSH traffic on port 22 was not opened to the entire internet because SSH provides administrative access.
- Administrative access should be restricted to trusted sources when required.
- The security group was used to control inbound network traffic to the EC2 instance.
- The VPC provided an isolated networking environment for the web server.
## Troubleshooting

I practiced troubleshooting connectivity by checking the EC2 instance's public IP address and public DNS, security group rules, route table configuration, subnet association, Internet Gateway attachment, and Apache web server configuration.

This helped me understand how network traffic travels from the internet through the AWS VPC to the EC2 web server.

When troubleshooting a publicly accessible web server, I learned that connectivity depends on multiple components working together, including routing, network access controls, and the server itself.
## What I Learned

Through this project, I learned how to:

- Create and configure an Amazon VPC.
- Create and configure a public subnet.
- Attach and configure an Internet Gateway.
- Create and configure a route table.
- Associate a subnet with a route table.
- Create and configure an EC2 security group.
- Launch an EC2 instance inside a VPC.
- Use EC2 User Data to automate server configuration.
- Install and configure an Apache web server.
- Understand basic AWS network traffic flow.
- Troubleshoot basic connectivity issues.
- Apply the principle of least privilege to network access.
## Project Outcome

Successfully deployed a publicly accessible web server inside a custom AWS VPC.

The EC2 instance successfully served a webpage through its public IP address, demonstrating connectivity between the internet, Internet Gateway, route table, public subnet, security group, and EC2 web server.

This project provided hands-on experience with AWS networking, compute, security, and basic web server deployment.
## Interview Talking Points

### Project Summary

I built and deployed a web server using Amazon VPC and Amazon EC2. I created a custom VPC, configured a public subnet, Internet Gateway, route table, and security group, then launched an EC2 web server and used EC2 User Data to automatically install and configure Apache.

### Security

I allowed HTTP traffic on port 80 because the web server was intended to be publicly accessible. I did not allow SSH from the entire internet because port 22 provides administrative access and should be restricted to trusted sources according to the principle of least privilege.

### Troubleshooting

I learned to troubleshoot connectivity by checking the EC2 instance's public IP and DNS, security group rules, route table, subnet association, Internet Gateway, and Apache web server configuration.

### Key Takeaway

This project gave me hands-on experience building an AWS network from the ground up and understanding how the different components work together to deliver a publicly accessible application.
