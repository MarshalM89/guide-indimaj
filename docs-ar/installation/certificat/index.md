# المرحلة 2 — إنشاء الشهادة وحفظها

!!! warning "متصفح إلزامي"
    يجب إنجاز هذه المرحلة بواسطة **Firefox 52 ESR**: لا يسمح Basilisk بتثبيت الشهادة.

## الخطوة 4 — الدخول إلى بوابة الشهادة { #etape-4 }

<figure markdown="span">
  ![بوابة الشهادة](portail-certificat.png){ width="760" }
  <figcaption>https://certificat.tgr.gov.ma</figcaption>
</figure>

1. في **Firefox**، ادخل إلى العنوان **[https://certificat.tgr.gov.ma](https://certificat.tgr.gov.ma){ target="_blank" }**.
2. أدخل **Identifiant GIP** (المعرّف) و **Code de génération** (رمز الإنشاء).
3. اضغط على **OK**.

!!! info "معلومة مفيدة"
    عادةً ما يكون المعرّف GIP ورمز الإنشاء مطابقين لاسم المستخدم في INDIM@J.

## الخطوة 5 — إنشاء الشهادة { #etape-5 }

<figure markdown="span">
  ![إنشاء الشهادة](enroll.png){ width="760" }
  <figcaption>EJBCA Firefox Certificate Enrollment</figcaption>
</figure>

1. اترك الملف التعريفي المقترح افتراضياً: **ENDUSER_TGR_AUTH_ET_SIGN**.
2. اضغط على **Enroll**.
3. تؤكد صفحة **Certificate Created** إنشاء الشهادة.
4. تظهر رسالة تفيد بأن الشهادة الشخصية قد ثُبّتت: اضغط على **OK**.

<figure markdown="span">
  ![تم إنشاء الشهادة](certificat-cree.png){ width="760" }
  <figcaption>النتيجة المنتظرة: تُنشأ الشهادة ثم تُثبّت تلقائياً في Firefox</figcaption>
</figure>

## الخطوة 6 — فتح مدير الشهادات في Firefox { #etape-6 }

<figure markdown="span">
  ![مدير الشهادات في Firefox](firefox-certificats.png){ width="760" }
  <figcaption>Firefox › Options › Avancé › Certificats</figcaption>
</figure>

1. افتح القائمة **☰** أعلى نافذة Firefox.
2. اضغط على **Options**.
3. اضغط على **Avancé**…
4. … ثم على تبويب **Certificats**.
5. اضغط على **Afficher les certificats**.

## الخطوة 7 — حفظ الشهادة { #etape-7 }

<figure markdown="span">
  ![حفظ الشهادة](sauvegarde.png){ width="760" }
  <figcaption>Gestionnaire de certificats › Vos certificats</figcaption>
</figure>

1. اضغط على تبويب **Vos certificats**.
2. اختر **الشهادة الجديدة**.
3. اضغط على **Sauvegarder…**
4. اختر مكان الحفظ، وأعطِ اسماً للملف، ثم اضغط على **Enregistrer**.
5. أدخل **كلمة مرور الحفظ** مرتين (يمكن ترك الخانتين فارغتين)، ثم اضغط على **OK**.
6. تظهر رسالة **Sauvegarde des certificats et clés privées réussie** (تم حفظ الشهادات والمفاتيح الخاصة بنجاح): اضغط على **OK**.

<figure markdown="span">
  ![كلمة مرور الحفظ](mot-de-passe-sauvegarde.png){ width="560" }
  <figcaption>كلمة مرور الحفظ</figcaption>
</figure>

<figure markdown="span">
  ![تم الحفظ بنجاح](sauvegarde-reussie.png){ width="560" }
  <figcaption>النتيجة المنتظرة: تم حفظ الشهادة والمفاتيح الخاصة بنجاح</figcaption>
</figure>

!!! warning "تذكّر"
    سجّل مكان الملف (.p12) وكلمة مرور الحفظ: ستُطلب منك في [الخطوة 12](../java/index.md#etape-12).
