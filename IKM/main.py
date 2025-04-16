import time
import poly, strassen, catalan


def main():
    print("\n№1:")
    time_track(poly.example)

    print("\n№2:")
    time_track(strassen.example)

    print("\n№5:")
    print("\tБиномиальный метод:")
    time_track(catalan.example_binom)
    print("\tМетод с сохранением промежуточных результатов:")
    time_track(catalan.example_dp)
    print("\tРекурсивный метод:")
    time_track(catalan.example_recursive)
    print()


def time_track(func):
    start_time = time.time()
    func()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time}")


if __name__ == "__main__":
    main()
