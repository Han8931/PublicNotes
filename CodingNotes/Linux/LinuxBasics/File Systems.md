# File Systems
## _ext_ filesystem
The original filesystem introduced with the Linux operating system was called the _extended filesystem_ (or just _ext_ for short). It provided a basic Unix-like filesystem for Linux, using virtual directories to handle physical devices and storing data in fixed-length blocks on the physical devices. 

The ext filesystem used a system called _inodes_ to track information about the files stored in the virtual directory. The inode system created a separate table on each physical device, called the inode table, to store file information. Each stored file in the virtual directory had an entry in the inode table. The extended part of the name comes from the additional data that it tracked on each file, which consisted of these items:

# Working with Filesystems

## Creating Partitions
To start out, you need to create a _partition_ on the storage device to contain the filesystem. The partition can be an entire disk or a subset of a disk that will contain a portion of the virtual directory.

Sometimes, the hardest part of creating a new disk partition is trying to find the physical disk on your Linux system. Linux uses a standard format for assigning device names to hard drives, and you need to be familiar with the format before partitioning a drive:
- SATA drives and SCSI drives: Linux uses `/dev/sd x`, where x is a letter based on the order in which the drive is detected (a for the first drive, b for the second, and so on)
- SSD NVMe drives: The device name format is `/dev/nvme N n #`, where N is a number based on the order in which the drive is detected, starting at 0 . And the # is the number assigned to the drive's namespace structure, starting at 1 .
- IDE drives: Linux uses `/dev/hd x`, where x is a letter based on the order in which the drive is detected (a for the first drive, b for the second, and so on).

### The fdisk utility

The _fdisk_ utility is an older but powerful tool for creating and managing partitions on any drive. However, fdisk handles only disks up to 2 TB in size. If you have a disk larger than that, you can use either the gdisk or the GNU parted utility instead.