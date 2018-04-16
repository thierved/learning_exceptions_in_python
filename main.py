
def security():
    try:
        pass_code = str(input('Enter the security code :'))

        if pass_code == '':
            raise ValueError('can\'t be empty!')
        
        if pass_code != 'the guard':
            raise Exception('wrong pass code !')

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)
    
    else :   
        print('wellcome to the system!')


def main():
    security()

if __name__ == '__main__': main()
