#3 posts, some discs, move them to the destination post using the auxiliary post
#when necessary with regard to other. No big disc must be on a smaller disc anytime.
def towers_hanoi(disc, src, aux, dst):
    if disc > 0:
        towers_hanoi(disc-1, src, dst, aux)
        print("move disc", disc, "from", src, "to", dst)
        towers_hanoi(disc-1, aux, src, dst)

d = input("The number of discs you want to use in your towers of hanoi puzzle: ")

di = int(d)
towers_hanoi(di, "SRC", "AUX", "DST")

#no defensive prog here o. I'm practising recursion. It's still confusing though
end = input("Press the 'Enter' Key")
