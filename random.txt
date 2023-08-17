for i in {1..10};
do
	mkdir d$i
	cd d$i
	for j in {1..15};
	do
		file_name=“file_$j.txt”
		for((k=1; k<j; k++));
		do
			echo “hello its random text for test $k” >> $file_name
		done
	done
	cd ..
done









