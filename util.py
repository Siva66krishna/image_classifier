"""
Parameters:
	dir_name: Directory name
Returns:
	directory name appended with "/", if not present 
"""
def format_dir_name(dir_name):
	if (dir_name.endswith("/")):
		return dir_name
	else:
		return dir_name + "/"

if __name__ == "__main__":
	test_name_1 = format_dir_name("test_dir/")
	assert test_name_1 == "test_dir/"

	test_name_2 = format_dir_name("test_dir")
	assert test_name_1 == "test_dir/"