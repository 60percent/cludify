variable "region" {
    default = "us-west-1"
}

variable "availability_zone" {
    default = "us-west-1b"
}

variable "vpc_cidr" {
    default = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
    default = "10.0.0.0/24"
}

provider "aws" {
  region = "${var.region}"
}

resource "aws_vpc" "vpc" {
    cidr_block = "${var.vpc_cidr}"
}

resource "aws_internet_gateway" "internet_gateway" {
    vpc_id = "${aws_vpc.vpc.id}"
}

resource "aws_subnet" "public_subnet" {
    cidr_block = "${var.public_subnet_cidr}"
    vpc_id = "${aws_vpc.vpc.id}"
    depends_on = ["aws_internet_gateway.internet_gateway"]    
    availability_zone = "${var.availability_zone}"
}

resource "aws_instance" "instance" {
    ami = "ami-65e0e305"
    instance_type = "t2.micro"
    private_ip = "10.0.0.4"
    subnet_id = "${aws_subnet.public_subnet.id}"
    availability_zone = "${var.availability_zone}"
}

resource "aws_eip" "eip" {
    vpc = true
    instance = "${aws_instance.instance.id}"
    associate_with_private_ip = "10.0.0.4"
    depends_on = ["aws_internet_gateway.internet_gateway"]  
}

output "instance_id" {
    value = "${aws_instance.instance.id}"
}
