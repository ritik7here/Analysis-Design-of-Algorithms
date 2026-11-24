
# Merge Sort for parcel prioritization

def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        # Compare priority first, then deadline, then ID
        key_left = (
            left[i]["priority"],
            left[i]["deadline"],
            left[i]["parcel_id"]
        )

        key_right = (
            right[j]["priority"],
            right[j]["deadline"],
            right[j]["parcel_id"]
        )

        if key_left <= key_right:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(parcels):

    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    return merge(left, right)
