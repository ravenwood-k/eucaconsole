# -*- coding: utf-8 -*-
# Copyright 2013-2017 Ent. Services Development Corporation LP
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Common constants for CloudWatch

"""
from ..i18n import _


METRIC_TYPES = [
    # NOTE: AWS/AutoScaling metrics expect 'None' (not 'Count' or None) as the unit
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupDesiredCapacity', 'unit': 'None'},
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupInServiceInstances', 'unit': 'None'},
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupMaxSize', 'unit': 'None'},
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupMinSize', 'unit': 'None'},
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupPendingInstances', 'unit': 'None'},
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupTerminatingInstances', 'unit': 'None'},
    {'namespace': 'AWS/AutoScaling', 'name': 'GroupTotalInstances', 'unit': 'None'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeWriteOps', 'unit': 'Count'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeWriteBytes', 'unit': 'Bytes'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeQueueLength', 'unit': 'Count'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeIdleTime', 'unit': 'Seconds'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeReadOps', 'unit': 'Count'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeReadBytes', 'unit': 'Bytes'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeTotalWriteTime', 'unit': 'Seconds'},
    {'namespace': 'AWS/EBS', 'name': 'VolumeTotalReadTime', 'unit': 'Seconds'},
    {'namespace': 'AWS/EC2', 'name': 'CPUUtilization', 'unit': 'Percent'},
    {'namespace': 'AWS/EC2', 'name': 'DiskReadBytes', 'unit': 'Bytes'},
    {'namespace': 'AWS/EC2', 'name': 'DiskReadOps', 'unit': 'Count'},
    {'namespace': 'AWS/EC2', 'name': 'DiskWriteBytes', 'unit': 'Bytes'},
    {'namespace': 'AWS/EC2', 'name': 'DiskWriteOps', 'unit': 'Count'},
    {'namespace': 'AWS/EC2', 'name': 'NetworkIn', 'unit': 'Bytes'},
    {'namespace': 'AWS/EC2', 'name': 'NetworkOut', 'unit': 'Bytes'},
    {'namespace': 'AWS/EC2', 'name': 'StatusCheckFailed', 'unit': 'Count'},
    {'namespace': 'AWS/EC2', 'name': 'StatusCheckFailed_Instance', 'unit': 'Count'},
    {'namespace': 'AWS/EC2', 'name': 'StatusCheckFailed_System', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'RequestCount', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'Latency', 'unit': 'Seconds'},
    {'namespace': 'AWS/ELB', 'name': 'UnHealthyHostCount', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HealthyHostCount', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HTTPCode_ELB_4XX', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HTTPCode_ELB_5XX', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HTTPCode_Backend_2XX', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HTTPCode_Backend_3XX', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HTTPCode_Backend_4XX', 'unit': 'Count'},
    {'namespace': 'AWS/ELB', 'name': 'HTTPCode_Backend_5XX', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'ComputeCoreAvailable', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'ComputeCoreTotal', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'ComputeDiskAvailable', 'unit': 'Gigabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'ComputeDiskTotal', 'unit': 'Gigabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'ComputeMemoryAvailable', 'unit': 'Megabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'ComputeMemoryTotal', 'unit': 'Megabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'InstanceTypeAvailable', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'InstanceTypeTotal', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'PublicIpTypeAvailable', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'PublicIpTypeTotal', 'unit': 'Count'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'StorageEbsAvailable', 'unit': 'Gigabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'StorageEbsTotal', 'unit': 'Gigabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'StorageObjectAvailable', 'unit': 'Gigabytes'},
    {'namespace': 'AWS/EucalyptusCapacity', 'name': 'StorageObjectTotal', 'unit': 'Gigabytes'},
]


# Maps simplified dimension keys to dimension names (for dict key in MetricAlarm().dimensions attr)
METRIC_DIMENSION_NAMES = {
    'availability_zone': 'AvailabilityZone',
    'image': 'ImageId',
    'instance': 'InstanceId',
    'instance_type': 'InstanceType',
    'load_balancer': 'LoadBalancerName',
    'scaling_group': 'AutoScalingGroupName',
    'volume': 'VolumeId',
}

# Maps simplified dimension keys to dimension input fields (in forms.alarms.CloudWatchAlarmCreateForm)
METRIC_DIMENSION_INPUTS = {
    'availability_zone': 'availability_zone',
    'image': 'image_id',
    'instance': 'instance_id',
    'instance_type': 'instance_type',
    'load_balancer': 'load_balancer_name',
    'scaling_group': 'scaling_group_name',
    'volume': 'volume_id',
}

# Maps metric names to friendly titles, primarily for CloudWatch charts
METRIC_TITLE_MAPPING = {
    # EC2 Metrics
    'CPUUtilization': _(u'CPU utilization'),
    'DiskReadBytes': _(u'Disk read bytes'),
    'DiskReadOps': _(u'Disk read ops'),
    'DiskWriteBytes': _(u'Disk write bytes'),
    'DiskWriteOps': _(u'Disk write ops'),
    'NetworkIn': _(u'Network in'),
    'NetworkOut': _(u'Network out'),
    'StatusCheckFailed': _(u'Status check failed (either)'),
    'StatusCheckFailed_Instance': _(u'Status check failed (instance)'),
    'StatusCheckFailed_System': _(u'Status check failed (system)'),
    # ELB Metrics
    'RequestCount': _(u'Request count'),
    'Latency': _(u'Latency'),
    'UnHealthyHostCount': _(u'Unhealthy hosts'),
    'HealthyHostCount': _(u'Healthy hosts'),
    'HTTPCode_ELB_4XX': _(u'Sum ELB 4xxs'),
    'HTTPCode_ELB_5XX': _(u'Sum ELB 5xxs'),
    'HTTPCode_Backend_2XX': _(u'Sum HTTP 2xxs'),
    'HTTPCode_Backend_3XX': _(u'Sum HTTP 3xxs'),
    'HTTPCode_Backend_4XX': _(u'Sum HTTP 4xxs'),
    'HTTPCode_Backend_5XX': _(u'Sum HTTP 5xxs'),
    # EBS Metrics
    'VolumeConsumedReadWriteOps': _(u'Volume consumed read/write operations'),
    'VolumeIdleTime': _(u'Volume idle time'),
    'VolumeQueueLength': _(u'Volume queue length'),
    'VolumeReadBytes': _(u'Volume read bytes'),
    'VolumeReadOps': _(u'Volume read ops'),
    'VolumeThroughputPercentage': _(u'Volume throughput percentage'),
    'VolumeTotalReadTime': _(u'Volume total read time'),
    'VolumeTotalWriteTime': _(u'Volume total write time'),
    'VolumeWriteBytes': _(u'Volume write bytes'),
    'VolumeWriteOps': _(u'Volume write ops'),
    # Scaling Group Metrics
    'GroupDesiredCapacity': _(u'Group desired capacity'),
    'GroupInServiceInstances': _(u'Group in service instances'),
    'GroupMaxSize': _(u'Group max size'),
    'GroupMinSize': _(u'Group min size'),
    'GroupPendingInstances': _(u'Group pending instances'),
    'GroupTerminatingInstances': _(u'Group terminating instances'),
    'GroupTotalInstances': _(u'Group total instances'),
    # SQS Metrics
    'NumberOfMessagesDeleted': _(u'Number of messages deleted'),
    'NumberOfMessagesSent': _(u'Number of messages sent'),
    'NumberOfMessagesReceived': _(u'Number of messages received'),
    'NumberOfEmptyReceives': _(u'Number of empty receives'),
    'ApproximateNumberOfMessagesDelayed': _(u'Approximate number of messages delayed'),
    'ApproximateNumberOfMessagesVisible': _(u'Approximate number of messages visible'),
    'ApproximateNumberOfMessagesNotVisible': _(u'Approximate number of messages not visible'),
    'ApproximateAgeOfOldestMessage': _(u'Approximate age of oldest message'),
    'SentMessageSize': _(u'Sent message size')
}

# Statistic choices for CloudWatch charts
STATISTIC_CHOICES = [
    ('Average', _(u'Average')),
    ('Minimum', _(u'Minimum')),
    ('Maximum', _(u'Maximum')),
    ('Sum', _(u'Sum')),
    ('SampleCount', _(u'Data samples')),
]

# Durations for CloudWatch charts (e.g. on Instance monitoring page)
MIN = 60  # seconds
FIVE_MIN = MIN * 5
FIFTEEN_MIN = MIN * 15
HOUR = 3600
DAY = HOUR * 24
THREE_HOURS = HOUR * 3
SIX_HOURS = HOUR * 6
TWELVE_HOURS = HOUR * 12
THREE_DAYS = DAY * 3
SEVEN_DAYS = DAY * 7
FOURTEEN_DAYS = DAY * 14

MONITORING_DURATION_CHOICES = [
    (HOUR, _(u'Last hour')),
    (THREE_HOURS, _(u'Last 3 hours')),
    (SIX_HOURS, _(u'Last 6 hours')),
    (TWELVE_HOURS, _(u'Last 12 hours')),
    (DAY, _(u'Last day')),
    (THREE_DAYS, _(u'Last 3 days')),
    (SEVEN_DAYS, _(u'Last 1 week')),
    (FOURTEEN_DAYS, _(u'Last 2 weeks')),
]

GRANULARITY_CHOICES = [
    (FIVE_MIN, _(U'5 minutes')),
    (FIFTEEN_MIN, _(U'15 minutes')),
    (HOUR, _(u'1 hour')),
    (SIX_HOURS, _(u'6 hours')),
    (DAY, _(u'1 day')),
]

# Trim granularity choices when longer durations are selected to avoid exceeding 1,440 data points limit in API
DURATION_GRANULARITY_CHOICES_MAPPING = {
    HOUR: GRANULARITY_CHOICES[:2],
    THREE_HOURS: GRANULARITY_CHOICES[:3],
    SIX_HOURS: GRANULARITY_CHOICES[:3],
    TWELVE_HOURS: GRANULARITY_CHOICES[1:4],
    DAY: GRANULARITY_CHOICES[1:4],
    THREE_DAYS: GRANULARITY_CHOICES[2:],
    SEVEN_DAYS: GRANULARITY_CHOICES[2:],
    FOURTEEN_DAYS: GRANULARITY_CHOICES[2:],
}
