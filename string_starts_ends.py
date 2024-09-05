start_with = "server is working very good"

print(start_with.startswith("server"))
print(start_with.startswith("is", 7, len(start_with)))

ends_with = start_with

print(ends_with.endswith("good"))
print(ends_with.endswith("very", 0, len(start_with) - 5))

remove_prefix = "(((( check"

print(remove_prefix.removeprefix("(((( "))

remove_suffix = "check/[/["

print(remove_suffix.removesuffix("/[/["))

partition = "this is python start and ends with functions"

print(partition.partition("python"))

r_partition = partition

print(r_partition.rpartition("ends"))