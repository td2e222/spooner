def calculate_area(length, width):
  area = length * width
  return area


def calculate_perimeter(length, width):
  perimeter = 2 * (length + width)
  return perimeter


def calculate_volume(length, width, height):
  volume = length * width * height
  return volume


def calculate_surface_area(length, width, height):
  surface_area = 2 * (length * width + length * height + width * height)
  return surface_area

def calculate_area_perimeter(length, width):
  area = length * width
  perimeter = 2 * (length + width)
  return area, perimeter


def main():
  area, perimeter = calculate_area_perimeter(5,10);
  print(area, perimeter)

if __name__ == '__main__':
  main()
