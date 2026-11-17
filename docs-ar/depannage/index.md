# حل المشاكل

تُستعمل هذه البطاقات فقط إذا لم يعمل INDIM@J بشكل صحيح بعد التثبيت.

!!! tip "انتهت صلاحية الشهادة؟"
    إذا عرض Firefox الرمز `SSL_ERROR_EXPIRED_CERT_ALERT`، فاتبع بدلاً من ذلك دليل [تجديد الشهادة](../renouvellement/index.md).

## أ — إفراغ الملفات المؤقتة لـ Java { #dep-a }

<figure markdown="span">
  ![إعدادات الملفات المؤقتة](cache-java-parametres.png){ width="760" }
  <figcaption>Java › Général › Paramètres des fichiers temporaires (الخطوات الفرعية من 1 إلى 3)</figcaption>
</figure>

1. في لوحة Java، تبويب **Général**، اضغط على **Paramètres…** (Fichiers Internet temporaires).
2. اضغط على **Supprimer les fichiers…** ثم أكّد.
3. ضع مؤشر مساحة القرص على **0**، ثم اضغط على **OK**.
4. اضغط على **Appliquer**.
5. أعد فتح **Paramètres…** وأرجع حجم التخزين إلى قيمته السابقة، ثم اضغط على **OK**.
6. اضغط مرة أخرى على **Appliquer**.

<figure markdown="span">
  ![تطبيق التعديل](cache-java-appliquer.png){ width="560" }
  <figcaption>تطبيق التعديل (الخطوة الفرعية 4)</figcaption>
</figure>

<figure markdown="span">
  ![إرجاع حجم التخزين](cache-java-retablir.png){ width="560" }
  <figcaption>إرجاع حجم التخزين (الخطوتان الفرعيتان 5 و 6)</figcaption>
</figure>

## ب — التأكد من وجود إصدار واحد فقط من Java { #dep-b }

<figure markdown="span">
  ![إصدارات Java المثبتة](versions-java.png){ width="760" }
  <figcaption>Java › onglet Java › Visualiser</figcaption>
</figure>

1. في لوحة Java، اضغط على تبويب **Java** ثم على **Visualiser…**
2. تأكد من ظهور **سطر واحد فقط** في اللائحة.
3. إذا ظهرت عدة إصدارات، احذف الإصدارات الأخرى عبر **Panneau de configuration** › **Programmes et fonctionnalités**.

!!! info "المشكل مستمر؟"
    اتصل بفريق INDIM@J: [equipe_indimaj@tgr.gov.ma](mailto:equipe_indimaj@tgr.gov.ma)
