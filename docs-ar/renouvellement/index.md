# تجديد الشهادة

يمكّنك هذا الدليل من استبدال شهادة ولوج منتهية الصلاحية، في 7 خطوات.

!!! warning "متصفح إلزامي"
    يجب إنجاز التجديد بواسطة **Firefox 52 ESR**: لا يسمح Basilisk بتثبيت الشهادة.

## الخطوة 1 — التعرف على شهادة منتهية الصلاحية { #r1 }

<figure markdown="span">
  ![فشل الاتصال الآمن](certificat-expire.png){ width="760" }
  <figcaption>https://indimaj.tgr.gov.ma — Échec de la connexion sécurisée</figcaption>
</figure>

!!! danger "الرسالة التي يعرضها Firefox"
    عند الدخول إلى INDIM@J (أو إلى INDIM@J Partenaire)، يعرض Firefox رسالة **« Échec de la connexion sécurisée »** مع النص *« Le pair SSL a rejeté votre certificat car celui-ci a expiré »* ورمز الخطأ `SSL_ERROR_EXPIRED_CERT_ALERT`.

!!! info "ماذا تفعل؟"
    انتهت صلاحية شهادة الولوج الخاصة بك. الضغط على «Réessayer» لا يحل المشكل: جدّد الشهادة باتباع الخطوات أسفله.

## الخطوة 2 — الدخول إلى بوابة الشهادة { #r2 }

<figure markdown="span">
  ![بوابة الشهادة](../installation/certificat/portail-certificat.png){ width="760" }
  <figcaption>https://certificat.tgr.gov.ma</figcaption>
</figure>

1. في **Firefox**، ادخل إلى العنوان **[https://certificat.tgr.gov.ma](https://certificat.tgr.gov.ma){ target="_blank" }**.
2. أدخل **Identifiant GIP** (المعرّف) و **Code de génération** (رمز الإنشاء).
3. اضغط على **OK**.

!!! info "معلومة مفيدة"
    عادةً ما يكون المعرّف GIP ورمز الإنشاء مطابقين لاسم المستخدم في INDIM@J.

## الخطوة 3 — إنشاء الشهادة الجديدة { #r3 }

<figure markdown="span">
  ![إنشاء الشهادة](../installation/certificat/enroll.png){ width="760" }
  <figcaption>EJBCA Firefox Certificate Enrollment</figcaption>
</figure>

1. اترك الملف التعريفي المقترح افتراضياً: **ENDUSER_TGR_AUTH_ET_SIGN**.
2. اضغط على **Enroll**.
3. تؤكد صفحة **Certificate Created** إنشاء الشهادة.
4. تظهر رسالة تفيد بأن الشهادة الشخصية قد ثُبّتت: اضغط على **OK**.

<figure markdown="span">
  ![تم إنشاء الشهادة](../installation/certificat/certificat-cree.png){ width="760" }
  <figcaption>النتيجة المنتظرة: تُنشأ الشهادة الجديدة ثم تُثبّت تلقائياً في Firefox</figcaption>
</figure>

## الخطوة 4 — فتح مدير الشهادات في Firefox { #r4 }

<figure markdown="span">
  ![مدير الشهادات في Firefox](../installation/certificat/firefox-certificats.png){ width="760" }
  <figcaption>Firefox › Options › Avancé › Certificats</figcaption>
</figure>

1. افتح القائمة **☰** أعلى نافذة Firefox.
2. اضغط على **Options**.
3. اضغط على **Avancé**…
4. … ثم على تبويب **Certificats**.
5. اضغط على **Afficher les certificats**.

## الخطوة 5 — حفظ الشهادة الجديدة { #r5 }

<figure markdown="span">
  ![حفظ الشهادة](../installation/certificat/sauvegarde.png){ width="760" }
  <figcaption>Gestionnaire de certificats › Vos certificats</figcaption>
</figure>

1. اضغط على تبويب **Vos certificats**.
2. اختر **الشهادة الجديدة** (الأحدث).
3. اضغط على **Sauvegarder…**
4. اختر مكان الحفظ، وأعطِ اسماً للملف، ثم اضغط على **Enregistrer**.
5. أدخل **كلمة مرور الحفظ** مرتين (يمكن ترك الخانتين فارغتين)، ثم اضغط على **OK**.
6. تظهر رسالة **Sauvegarde des certificats et clés privées réussie** (تم حفظ الشهادات والمفاتيح الخاصة بنجاح): اضغط على **OK**.

<figure markdown="span">
  ![كلمة مرور الحفظ](../installation/certificat/mot-de-passe-sauvegarde.png){ width="560" }
  <figcaption>كلمة مرور الحفظ</figcaption>
</figure>

<figure markdown="span">
  ![تم الحفظ بنجاح](../installation/certificat/sauvegarde-reussie.png){ width="560" }
  <figcaption>النتيجة المنتظرة: تم حفظ الشهادة والمفاتيح الخاصة بنجاح</figcaption>
</figure>

!!! warning "تذكّر"
    سجّل مكان الملف (.p12) وكلمة مرور الحفظ: ستُطلب منك في [الخطوة الأخيرة](#r7).

## الخطوة 6 — فتح لوحة Java والتحقق من الخيارات { #r6 }

<figure markdown="span">
  ![Configure Java](../installation/java/configurer-java.png){ width="560" }
  <figcaption>Windows › Menu Démarrer</figcaption>
</figure>

1. اضغط على زر **Démarrer** في Windows.
2. في خانة البحث، اكتب **configurer java**، ثم اضغط على **Configure Java**.
3. اضغط على تبويب **Avancé** وتحقق من **Paramètres de sécurité avancés** حسب الجدول أسفله.
4. اضغط على **Appliquer**. أبقِ لوحة Java مفتوحة.

<figure markdown="span">
  ![إعدادات الأمان المتقدمة](../installation/java/options-avancees.png){ width="560" }
  <figcaption>Java › Avancé › Paramètres de sécurité avancés</figcaption>
</figure>

| الخيار | الحالة |
|--------|------|
| Activer l'environnement restreint (natif) du système d'exploitation | <span class="opt-on">☑ مفعّل</span> |
| Utiliser les certificats et les clés du fichier de clés du navigateur | <span class="opt-on">☑ مفعّل</span> |
| Activer la vérification de révocation de la liste noire | <span class="opt-on">☑ مفعّل</span> |
| Activer la mise en cache du mot de passe pour l'authentification | <span class="opt-on">☑ مفعّل</span> |
| Utiliser le format ClientHello compatible SSL 2.0 | <span class="opt-off">☐ غير مفعّل</span> |
| Utiliser TLS 1.0 | <span class="opt-on">☑ مفعّل</span> |
| Utiliser TLS 1.1 | <span class="opt-on">☑ مفعّل</span> |
| Utiliser TLS 1.2 | <span class="opt-on">☑ مفعّل</span> |

## الخطوة 7 — استبدال الشهادة القديمة في Java { #r7 }

<figure markdown="span">
  ![استبدال الشهادة القديمة](remplacer-certificat.png){ width="760" }
  <figcaption>Java › Sécurité › Gérer les certificats</figcaption>
</figure>

1. اضغط على تبويب **Sécurité**.
2. اضغط على **Gérer les certificats…**
3. في **Type de certificat**، اختر **Authentification du client**.
4. اختر **الشهادة القديمة**.
5. اضغط على **Enlever**. إذا طُلبت كلمة مرور، اضغط على **OK**.
6. اضغط على **Importer**، ثم اختر **الشهادة الجديدة** التي حفظتها من Firefox.
7. أدخل **كلمة مرور الحفظ** الخاصة بالشهادة.
8. عندما تُطلب كلمة المرور مرة ثانية، اضغط على **OK** دون كتابة أي شيء.
9. اضغط على **Fermer**، ثم على **OK**.

!!! success "تم تجديد الشهادة"
    أغلق المتصفح ثم أعد فتحه، وادخل من جديد إلى INDIM@J.
