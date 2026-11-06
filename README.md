# Smartphone Activity Recognition
Classifies six everyday activities (walking, walking upstairs, walking downstairs, sitting, standing, laying) from a phone's accelerometer and gyroscope data.

Why

Most people already carry a phone, so recognizing activity from its sensors needs no extra wearable. We test every model on volunteers it has never seen and ask: does an SVM beat regularized logistic regression, and which activities get confused?

Dataset: Human Activity Recognition Using Smartphones (UCI). 10,299 windows from 30 volunteers wearing a phone at the waist, 561 features per window, 6 activity labels.

Research question: Under volunteer grouped 5 fold cross validation, does an SVM achieve a higher macro-F1 than regularized logistic regression, and which activities are most often confused?

Roadmap: Phase 1 proposal and EDA, Phase 2 baselines and stream replay, Phase 3 SVM vs. logistic regression with grouped CV, Phase 4 live demo and final report

Documentation & Contributing

Full details (related work, data plan, references) are in the project proposal. Course project (ML 402331) by Zaina Alnimer, Suleiman Dajani and Majd Jammoul. Phase 1 is done; baselines, SVM comparison and the live demo are next.
