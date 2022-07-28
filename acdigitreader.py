import csv
import matplotlib.pyplot as plt

def digitreader():
    base = 4
    digitslist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    while base < 17:
        basedigitslist = digitslist[0:base]
        frequencylist = [0] * len(basedigitslist)
        with open ('Cancellation Sheets' + '\\anomalouscancellationsinbase' + str(base) + '.csv') as csvfile:
            file = csv.reader(csvfile)
            for row in file:
                removalStr = row[4]
                #if len(removalStr) == 3:
                for element in removalStr:
                    try:
                        index = basedigitslist.index(element)
                        frequencylist[index] += 1
                    except ValueError:
                        pass
            fig, ax = plt.subplots()
            ax.set_xlabel('Digit')
            ax.set_ylabel('Percent Removals')
            ax.set_title('Removals by Digit in Base ' + str(base)) 
            total = sum(frequencylist)
            percentlist = [x / total for x in frequencylist]
            ax.bar(basedigitslist, percentlist)
            rects = ax.patches
            for rect, label in zip(rects, percentlist):
                height = rect.get_height()
                print(label)
                ax.text(rect.get_x() + rect.get_width()/2, height, str(label)[0:8], ha='center', va='bottom')
            filename = 'Probability Graphs/base' + str(base) + '.png'
            plt.savefig(filename)
        base += 1

if __name__ == "__main__":
    digitreader()