class vehicle(object):
    def __init__(self,steering,wheels,clutch,breaks,gears):
        self ._steering = steering
        self ._wheels = wheels
        self ._clutch = clutch
        self ._breaks = breaks
        self ._gears = gears

    #def __init__(self):
     #   print ('this is the distructor')

    def dsiplay_vehicle(self):
        print ('steering:', self ._steering)
        print ('wheels:', self ._wheels)
        print ('clutch:', self ._clutch)
        print ('breaks:', self ._breaks)
        print ('gears:', self ._gears)
myvehicle = vehicle(input(),input(),input(),input(),input())
myvehicle.dsiplay_vehicle()





