def konversi(w=0):
    def hari(h=0):
        def jam(j=0):
            def menit(m=0):
                return ((w * 7 + h)*24 + j)*60+m
            return menit
        return jam
    return hari


data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

data = list(map(lambda x: list(filter(str.isnumeric, x.split())), data))

print("data = ", data, end="\n\n")

# kegiatan 1
print("================ Kegiatan 1 ================")
answer = []

for i in data:
    minggu = int(i[0])
    hari = int(i[1])
    jam = int(i[2])
    menit = int(i[3])
    print("minggu = ", minggu, end="\t")
    print("hari = ", hari, end="\t")
    print("jam = ", jam, end="\t")
    print("menit = ", menit, end="\t")
    konvert = konversi(minggu)(hari)(jam)(menit)
    print(f"konversi ke menit : {konvert}")
    answer.append(konvert)

print(f"\n\n{answer}")

# kegiatan 2
print("\n\n================ Kegiatan 2 ================")
for i in data:
    print(i)
