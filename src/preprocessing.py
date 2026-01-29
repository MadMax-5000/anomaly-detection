import pandas as pd
import numpy as np
import os
import glob

# we will start with real AWS CloudWatch dataset
sensors = "C:\\Users\\yassi\\user-behavior-analysis\\data\\realAWSCloudwatch\\realAWSCloudwatch"

# loading data from csv
sensors = glob.glob(os.path.join(sensors, "*.csv"))
sensors_dfs = {}

for csv in sensors:
    name = os.path.splitext(os.path.basename(csv))[0]
    sensors_dfs[name] = pd.read_csv(csv)

# concatenating dataframes and oragnizing them
cpu_utilization = pd.concat(
    [
        sensors_dfs["ec2_cpu_utilization_24ae8d"],
        sensors_dfs["ec2_cpu_utilization_53ea38"],
        sensors_dfs["ec2_cpu_utilization_5f5533"],
        sensors_dfs["ec2_cpu_utilization_77c1ca"],
        sensors_dfs["ec2_cpu_utilization_825cc2"],
        sensors_dfs["ec2_cpu_utilization_ac20cd"],
        sensors_dfs["ec2_cpu_utilization_c6585a"],
        sensors_dfs["ec2_cpu_utilization_fe7f93"],
    ],
    ignore_index=True,
)
cpu_utilization["timestamp"] = pd.to_datetime(cpu_utilization["timestamp"])
cpu_utilization = cpu_utilization.sort_values("timestamp").reset_index(drop=True)

rds_cpu_utilization = pd.concat(
    [
        sensors_dfs["rds_cpu_utilization_cc0c53"],
        sensors_dfs["rds_cpu_utilization_e47b3b"],
    ],
    ignore_index=True,
)
rds_cpu_utilization["timestamp"] = pd.to_datetime(rds_cpu_utilization["timestamp"])
rds_cpu_utilization = rds_cpu_utilization.sort_values("timestamp").reset_index(
    drop=True
)


disk_write_bytes = pd.concat(
    [
        sensors_dfs["ec2_disk_write_bytes_1ef3de"],
        sensors_dfs["ec2_disk_write_bytes_c0d644"],
    ],
    ignore_index=True,
)
disk_write_bytes["timestamp"] = pd.to_datetime(disk_write_bytes["timestamp"])
disk_write_bytes = disk_write_bytes.sort_values("timestamp").reset_index(drop=True)

network_in = pd.concat(
    [
        sensors_dfs["ec2_network_in_257a54"],
        sensors_dfs["ec2_network_in_5abac7"],
        sensors_dfs["iio_us-east-1_i-a2eb1cd9_NetworkIn"],
    ],
    ignore_index=True,
)
network_in["timestamp"] = pd.to_datetime(network_in["timestamp"])
network_in = network_in.sort_values("timestamp").reset_index(drop=True)

request_count = sensors_dfs["elb_request_count_8c0756"]
request_count["timestamp"] = pd.to_datetime(request_count["timestamp"])
request_count = request_count.sort_values("timestamp").reset_index(drop=True)

grok_asg = sensors_dfs["grok_asg_anomaly"]
grok_asg["timestamp"] = pd.to_datetime(grok_asg["timestamp"])
grok_asg = grok_asg.sort_values("timestamp").reset_index(drop=True)
