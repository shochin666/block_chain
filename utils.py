import hashlib
import collections


def sorted_dict_by_key(unsorted_dict):
    """
    :param unsorted_dict:
    :return: キーの順序が保持されたままのdictが返り値です
    """
    return collections.OrderedDict(
        sorted(unsorted_dict.items(), key=lambda d: d[0])
    )


def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"=" * 25} Chain{i} {"=" * 25}')
        for k, v in chain.items():
            # {◯◯:15}で幅を指定
            if k == 'transactions':
                print(k)
                for d in v:
                    print('-' * 40)
                    for kk, vv in d.items():
                        print(f'{kk:30}{vv}')

            else:
                print(f'{k:15}{v}')

    print("*" * 25)
