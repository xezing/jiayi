#!/usr/bin/python3
import csv
import json

if __name__ == '__main__':
    outputFile = r"D:\workspace\jiayi\cctv_17\datatask\files\activeAlarms_20210801.csv"
    inputFile = r"D:\workspace\jiayi\cctv_17\datatask\files\activeAlarms_20210801000003.txt"
    with open(outputFile, "w", encoding="utf-8", newline="") as out:
        csv_writer = csv.writer(out)
        with open(inputFile, "r", encoding="utf-8") as f:
            for line in f:
                loads = json.loads(line)
                csv_writer.writerow([loads["objectName"],
                                     loads["nativeEMSName"],
                                     loads["nativeProbableCause"],
                                     loads["objectType"],
                                     loads["emsTime"],
                                     loads["neTime"],
                                     loads["isClearable"],
                                     loads["layerRate"],
                                     loads["probableCause"],
                                     loads["probableCauseQualifier"],
                                     loads["perceivedSeverity"],
                                     loads["serviceAffecting"],
                                     loads["additionalInfo"][7]["value"],
                                     loads["additionalInfo"][3]["value"],
                                     loads["additionalInfo"][9]["value"],
                                     loads["additionalInfo"][10]["value"],
                                     loads["X.733::EventType"],
                                     loads["objectTypeQualifier"],
                                     loads.get("rcaiIndicator", ""),
                                     loads["X.733::CorrelatedNotifications"],
                                     loads["X.733::ProposedRepairActions"],
                                     ])
