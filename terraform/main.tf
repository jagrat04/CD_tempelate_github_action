provider "aws" {
  region = "us-east-1"
}

variable "instance_count" {
  default = 3
}

resource "aws_instance" "web" {
  count         = var.instance_count
  ami           = "ami-0c2b8ca1dad447f8a" # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  key_name      = "ssh_key_name"

  tags = {
    Name = "web-${count.index}"
  }
}

resource "aws_security_group" "allow_http" {
  name_prefix = "http-"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_lb" "alb" {
  name               = "nginx-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.allow_http.id]
  subnets            = ["subnet-xxxxxxxx", "subnet-yyyyyyyy"] 
}

output "load_balancer_dns" {
  value = aws_lb.alb.dns_name
}
