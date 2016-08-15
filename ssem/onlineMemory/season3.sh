#for k in 50 100 200 300 400 500
for k in 1 40
do
	python season3.py 2013-10-19 2013-10-20 $k
	python season3.py 2013-10-20 2013-10-21 $k
	python season3.py 2013-10-21 2013-10-22 $k
	python season3.py 2013-10-22 2013-10-23 $k
	python season3.py 2013-10-23 2013-10-24 $k
	python season3.py 2013-10-24 2013-10-25 $k
	python season3.py 2013-10-25 2013-10-26 $k
	python season3.py 2013-10-26 2013-10-27 $k
done
