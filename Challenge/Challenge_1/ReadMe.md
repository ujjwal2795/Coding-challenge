---
description: This template allows you to deploy a 3 Tier architecture using 'Red Hat Enterprise Linux 7.3' virtual machines. Architecture includes Virtual Network, external and internal load balancers, Jump VM, NSGs etc along with multiple RHEL Virtual machines in each tier
page_type: sample
products:
- azure
- azure-resource-manager
urlFragment: rhel-3tier-iaas
languages:
- json
---
# Red Hat Linux 3-Tier Solution on Azure



1. [Solution Overview](#solution-overview)
2. [Template Solution Architecture ](#template-solution-architecture)
3. [Licenses and Costs ](#licenses-and-costs)
4. [Prerequisites](#prerequisites)
5. [Deployment Steps](#deployment-steps)
6. [Deployment Time](#deployment-steps)
7. [Post Deployment Steps](#post-deployment-steps)

<!-- /TOC -->

## Solution Overview
This Azure Quick Start template deploys a 3 Tier Red Hat Solution on Azure.The Solution includes Web tier Servers, Application tier Servers and Database Tier Servers running Red Hat Enterprise Linux 7.3. Template follows Standard best practices for running a 3 tier Red Hat Linux IaaS workload on Azure. This template will deploy specified number of VMs in each tier as per requirement.

## Template Solution Architecture

This template will deploy:

- Four storage accounts: 3 for storing VM's disks of each tier, 1 for storing diagnostics data.
- One Virtual Network with four subnets.
- 4 Network Security Group, one for each subnet.
- External Load Balancer to load balance Web Traffic(HTTP & HTTPS) to web servers.
- Internal Load Balancer to load balance traffic for app VM's.
- 2 Public IP’s, one for external Load balancer and other for Jump VM.
- 3 Virtual Machine Availability sets for Web Tier, Application Tier and Database tier.
- One Jump VM to faclitate ssh access to all other tier VMs.
- Multiple Red Hat Enterprise Linux VMs for each tier as per parameter value specified during deployment.

![Deployment Solution Architecture](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/application-workloads/redhat/rhel-3tier-iaas/images/architecture.png)

## Licenses and Costs

The Red Hat Enterprise Linux 7.3 image used in this solution is the PAYG model and doesn't require the user to license it, it will be licensed automatically after the instance is launched first time. Use of this image carries a separate hourly charge that is in addition to Microsoft's Linux VM rates. Total price of the VM consists of the base Linux VM price plus RHEL VM image surcharge.  Click [here](https://azure.microsoft.com/pricing/details/virtual-machines/red-hat/) for pricing details.

## Prerequisites

Azure Subscription with specified payment method (Red Hat Enterprise Linux is a market place product and requires payment method to be specified in Azure Subscription)

## Deployment Steps

Build your Red Hat 3-Tier IaaS environment on Azure in a two simple steps:
- Launch the Template deployment by clicking on Deploy to Azure button.
- Fill in all the required parameter values, Accept the terms and condition on click Purchase.

## Deployment Time

The deployment takes about 5 minutes to complete.

## Post Deployment Steps

After successful deployment, this template will output the IP address and FQDN of both external load balancer and Jump VM. Make a note of these values.

- To access all VM's via SSH, you need to first ssh into jump VM using its public ip captured from template outputs, from jump VM you can ssh into other VMs through via private IP.
- Alternatively You can also get public IP of Jump VM from overview blade in VM Settings.
- Load balancer is configured for load balancing HTTP(Port 80) and HTTPS(Port 443) to distribute traffic to web servers.You can configure web servers and start accessing websites using Load Balancer.

