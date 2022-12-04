import subprocess
from io import StringIO
def main():
    with open('day04.txt', 'rt') as fobj:
        lines = fobj.readlines()
    arnold = []
    for line in lines:
        fst, snd = line.strip().split(',')
        a = fst.split('-')
        a += snd.split('-')
        arnold.append(a)

    arnold_filename = 'advent-2022-day04'
    subprocess.check_call(['java', '-jar', 'ArnoldC.jar', arnold_filename + '.arnoldc'])
    expect_filename = 'advent-2022-day04.exp'
    with open(expect_filename, 'wt') as fobj:
        fobj.write(f'spawn java {arnold_filename}\n')
        for a in arnold:
            for val in a:
                fobj.write(f'expect "next" {{ send "{val}\\n" }}\n')
        fobj.write('expect "next"\n')
    ret = subprocess.check_output(
        ['expect', expect_filename],
    )
    lines = ret.decode().split('\r\n')
    result = lines[-3]
    print(result)

if __name__ == '__main__':
    main()