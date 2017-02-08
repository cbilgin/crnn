#!/usr/bin/env python
import SimpleITK as itk
import sys


if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <InputImage> <OutputImage>")
    sys.exit(1)

PixelType = itk.UC
Dimension = 2

ImageType = itk.Image[PixelType, Dimension]

input = sitk.SetFileName(sys.argv[1])

flipFilter = itk.FlipImageFilter[ImageType].New()
flipFilter.SetInput(reader.GetOutput())
flipAxes = (True, False)
flipFilter.SetFlipAxes(flipAxes)
writer = itk.ImageFileWriter[ImageType].New()
writer.SetFileName(sys.argv[2]+"_x.png")
writer.SetInput(flipFilter.GetOutput())
writer.Update()

flipFilter1 = itk.FlipImageFilter[ImageType].New()
flipFilter1.SetInput(reader.GetOutput())
flipAxes = (False, True)
flipFilter1.SetFlipAxes(flipAxes)
writer1 = itk.ImageFileWriter[ImageType].New()
writer1.SetFileName(sys.argv[2]+"_y.png")
writer1.SetInput(flipFilter1.GetOutput())
writer1.Update()

