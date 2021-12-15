from evalys.jobset import JobSet
import matplotlib.pyplot as plt

test = "03"

js = JobSet.from_csv("./test{n}/test{n}_jobs.csv".format(n=test))

js.plot(with_details=True, )

plt.savefig("./test{n}/results{n}.png".format(n=test))