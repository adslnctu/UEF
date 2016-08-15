#for k in 50 100 200 300 400 500
for k in 1 30
do
	python season2.py 2013-06-06 2013-06-07 $k
	python season2.py 2013-06-07 2013-06-08 $k
	python season2.py 2013-06-08 2013-06-09 $k
	python season2.py 2013-06-09 2013-06-10 $k
	python season2.py 2013-06-10 2013-06-11 $k
	python season2.py 2013-06-11 2013-06-12 $k
done
