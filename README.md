# Research_work

One of the critical issues of the SkinCare application is the minimization of the false negative outputs.
Different methods may behave differently in their dependence from the databases. Such
dependence has been experienced in derm7pt and ISIC data and much larger dependencies have
been found when we compared ISIC data and data from Semmelweis University and   independence.
Such dependencies are not reported in the literature and they seriously jeopardize that application.
In our discussions with Degetel we agreed to make all efforts to limit this devastating effect that will
appear for different light conditions and different cameras of the different mobile phones. We are
trying different methods and will provide the best combination for Degetel. Our paper to be
submitted and titled as „Minimizing false negative rate in melanoma detection and providing insight
into the causes of classification” offers a potential route for the solution.

The critical issue of the SkinCare application is the minimization of the false negative
outputs. The task is the exploration of potential solutions for the minimization of false
negative rates by means of a series of evaluations using
  •	Use a deep neural network for classification. <br />
  •	By the help of NipgBoard* project the results of deep neural network classification into the 3D sphere.  <br />
  •	After the training with the help of the labels analyze the result of classification.  <br />
  •	Use different graph cutting to automatize the cluster searching method.  <br />
  •	Find those false negative clusters where quality is sufficient.  <br />
  •	Take out this samples from test and training dataset. <br />
  •	Make correction on the remining poor clusters by using KIRA.  <br />
  •	Use step 3-6 again.  <br />
  •	Start the training again on the remaining dataset.  <br />
Details of the task:
a. Do the evaluation on the ISIC dermoscopic data. Evaluate  <br />
b. Do the evaluation on the derm7pt macroscopic data. Evaluate  <br />
c. In case of reasonable achievement, provide the information and help to include the results into the Degetel software  <br />

*Nipgboard : NipgBoard is an extension and functionally modified version of Google's TensorBoard. It's online and interactive, it is meant to be a platform to combine the specific knowledge of experts from different scientific fields (AI, medication, dermatology, psychology, industrial experts and so on).
Useful links:
https://www.tensorflow.org/tensorboard
https://projector.tensorflow.org/
https://github.com/tensorflow/tensorboard


### Dataset :ISIC2019

