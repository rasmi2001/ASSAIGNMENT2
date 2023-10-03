provider "aws" {
  region = "us-east-1"  
}
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"  
  map_public_ip_on_launch = true
}
resource "aws_subnet" "private_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"  
}
resource "aws_security_group" "my_security_group" {
name        = "my-security-group"
description = "Security group for EC2 instance"
ingress {
    
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
vpc_id = aws_vpc.my_vpc.id
}
resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  key_name      = "your-key-pair-name"    
  associate_public_ip_address = true

  root_block_device {
    volume_type = "gp2"
    volume_size = 8
  }
tags = {
    "Name"    = "Assignment Instance"
    "purpose" = "Assignment"
  }
  vpc_security_group_ids = [aws_security_group.my_security_group.id]
}
