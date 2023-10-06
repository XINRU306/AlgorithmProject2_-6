
def main():
    # Define x with static scope in the outer function
    x=10
    # Simulating the dynamic scope of x value
    def dynamic_scope():
        nonlocal x
        x+=20

    # print x value
    print("Static scope for X value:", x)
    dynamic_scope()
    print("Dynamic scope for X value:", x)

# run whole function
if __name__ == '__main__':
    main()