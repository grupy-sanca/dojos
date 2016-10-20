# https://www.codewars.com/kata/take-a-picture/train/python
def sort_photos(pics):
    years = [pic.split('.')[0] for pic in pics]
    numbers = [int(pic.split('g')[-1]) for pic in pics]

    data = sorted(zip(years, numbers))[-5:]
    data.append((data[-1][0], data[-1][1] + 1))
    return ['{}.img{}'.format(year, number) for year, number in data]
