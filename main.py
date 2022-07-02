# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import pandas as pd
file_name = 'C:\\Users\\z004b00e\\Downloads\\ExceptionList.xlsx'
df = pd.read_excel(file_name, index_col=None, na_values=['NA'], usecols = "A")


# Using editdistance package to calculate the levenhstein distance between strings.
import editdistance as edist

import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import pairwise_distances

# Simple data (sample genome string).
data = ["TAU.Core.SUTException: Timed out while waiting for segment image to change. Afte\nr  millisecond the image did not change. (expected =  percent, actual = . percent). \n   at sdk.syngo.IS.TestAbstractions.Viewing.ImageAreaAccess.LocateSegment.WaitUn\ntilImageChangedInArea(Rectangle boundingRectangle, Action action, Int timeout, Single minimumPercentageToChange)\n   at sdk.syngo.IS.CommonTestSteps.TestSteps.SeriesNavigatorNew.Given.ItemWasLmbDragAndDroppedToSegment.ExecuteImpl()\n   at TAU.Framework.CSL.AbstractStepBase.<DoStep>b___()\n   at TAU.Driver.TestMon.DoStep(String stepId_in, Boolean shouldStopTest_in, Action step_in)", "TAU.Framework.UITestCommon.TimeoutTAUException: The following expectation has no\nt been met within ### Time ###: Wait for image text available  > System.TimeoutE\nxception: The following expectation has not been met within ### Time ###: Wait for image text available\n   at sdk.syngo.IS.ReusableAPIs.Utils.PollWaitTAUCopy.ThrowTimeoutExceptionUnlessSuppressed()\n   at sdk.syngo.IS.ReusableAPIs.Utils.PollWaitTAUCopy.DoPollSleepTimeoutCheck(Func` verification)\n   at sdk.syngo.IS.ReusableAPIs.Utils.Wait.Until(Expression` expr, Int timeout, Int interval, String descriptionOfWaitCondition, Boolean throwOnTimeout)\n    End of inner exception stack trace \n   at sdk.syngo.IS.ReusableAPIs.Utils.Wait.Until(Expression` expr, Int timeout, Int interval, String descriptionOfWaitCondition, Boolean throwOnTimeout)\n   at sdk.syngo.IS.CommonTestSteps.TestSteps.ImageText.Then.ImageTextShouldBeContainedIn.ExecuteImpl()\n   at TAU.Framework.CSL.AbstractStepBase.<DoStep>b___()\n...[Skipped 1 lines]", "System.IO.IOException: The process cannot access the file '### Link ###' because it is being used by another process.\n   at System.IO.__Error.WinIOError(Int errorCode, String maybeFullPath)\n   at System.IO.File.InternalDelete(String path, Boolean checkHost)\n   at TAU.Driver.TestMon.DoStep(String stepId_in, Boolean shouldStopTest_in, Action step_in)","System.IO.IOException: The process cannot access the file '### Link ###' because it is being used by another process.\n   at System.IO.__Error.WinIOError(Int errorCode, String maybeFullPath)\n   at System.IO.File.InternalDelete(String path, Boolean checkHost)\n   at TAU.Driver.TestMon.DoStep(String stepId_in, Boolean shouldStopTest_in, Action step_in)"]#df.values.tolist()

# Custom distance metric and use editdistance.
def lev_metric(x, y):
    return int(edist.eval(data[int(x[0])], data[int(y[0])]))

# Reshape the data.
X = np.arange(len(data)).reshape(-1, 1)
print(X.shape)

# Calculate pairwise distances with the new metric.
m = pairwise_distances(X, X, metric=lev_metric)
print(m)

# Perform agglomerative clustering.
# The affinity is precomputed (since the distance are precalculated).
# Use an 'average' linkage. Use any other apart from  'ward'.
agg = AgglomerativeClustering(n_clusters=3, affinity='precomputed',
                              linkage='average')

# Use the distance matrix directly.
u = agg.fit_predict(m)
print(u)