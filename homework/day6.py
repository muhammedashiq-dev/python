blog_views = [150,800,2500,600,1200,450,3000]
trending = 0
total_views = 0
for x in blog_views:
    print(x)
    if x > 1000:
        print('blog is trending')
        trending += 1
    elif x >= 500 and x < 1000:
        print('blog is average')
    else:
        print('low traffic')
    total_views += x
print('trending:',trending)
print('total views',total_views)