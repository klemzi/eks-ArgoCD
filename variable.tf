# Cluster section
variable "cluster_name" {
  type    = string
  default = "klem-cluster"
}
# Networking section
variable "vpc_id" {
  type        = string
  default     = "vpc-094bc4438422a9768"
  description = "ID of the vpc where the cluster will reside in"
}

variable "subnet_ids" {
  type        = list(string)
  default     = ["subnet-06ce892165cc21e2f", "subnet-092913c8d91ea275e"]
  description = "List subnet ids where node groups will be provisioned"
}
