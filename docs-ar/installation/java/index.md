# المرحلة 3 — تثبيت Java وإعداده

## الخطوة 8 — تثبيت Java 8 (32 bits) { #etape-8 }

[:material-download: jre-8u60-windows-i586.exe](https://drive.google.com/drive/folders/1UZJvKztSVTUchLILuPxfFBg5bT1W3Tur?usp=drive_link){ .md-button .md-button--primary .dl target="_blank" }

1. حمّل الملف `jre-8u60-windows-i586.exe` من [مجلد Google Drive الخاص بملفات التثبيت](https://drive.google.com/drive/folders/1UZJvKztSVTUchLILuPxfFBg5bT1W3Tur?usp=drive_link){ target="_blank" }.
2. انقر مرتين على الملف الذي تم تحميله.
3. اتبع مراحل التثبيت إلى النهاية.

!!! info "نسخة 32 bits"
    بما أن Firefox 52 ESR و Basilisk متصفحان بنسخة 32 bits، يجب أن يكون Java أيضاً بنسخة 32 bits، حتى على Windows بنسخة 64 bits.

!!! warning "إذا كنت تستعمل Basilisk"
    يجب تثبيت Basilisk **قبل** Java ([الخطوة 3](../navigateurs/index.md#etape-3)) حتى تُضاف وحدة Java إلى المتصفح.

## الخطوة 9 — السماح بالكتابة في مجلد Java { #etape-9 }

<figure markdown="span">
  ![صلاحيات الكتابة في مجلد Java](droits-ecriture.png){ width="560" }
  <figcaption>Propriétés de : Java › Sécurité</figcaption>
</figure>

1. افتح المجلد **C:\Program Files (x86)** (أو **C:\Program Files** على Windows بنسخة 32 bits).
2. انقر بالزر الأيمن على مجلد **Java** › **Propriétés** › تبويب **Sécurité**.
3. اختر مجموعة **Utilisateurs** ثم اضغط على **Modifier…**
4. ضع علامة في خانة **Autoriser** بالنسبة لـ **Modification** و **Écriture**، كما في الصورة.
5. اضغط على **Appliquer** ثم على **OK**.

## الخطوة 10 — فتح لوحة إعدادات Java { #etape-10 }

<figure markdown="span">
  ![Configure Java](configurer-java.png){ width="560" }
  <figcaption>Windows › Menu Démarrer</figcaption>
</figure>

1. اضغط على زر **Démarrer** في Windows.
2. في خانة البحث، اكتب **configurer java**.
3. اضغط على **Configure Java**.

!!! info "للعلم"
    تُستعمل هذه اللوحة حتى نهاية هذه المرحلة. أبقِها مفتوحة.

## الخطوة 11 — إضافة INDIM@J إلى المواقع المسموح بها في Java { #etape-11 }

<figure markdown="span">
  ![لائحة المواقع المستثناة](sites-exception.png){ width="760" }
  <figcaption>Java › Sécurité › Liste des sites avec exception</figcaption>
</figure>

1. اضغط على تبويب **Sécurité**.
2. اضغط على **Modifier la liste des sites…**
3. اضغط على **Ajouter** واكتب **https://indimaj.tgr.gov.ma**.
4. اضغط على **OK** للتأكيد.

!!! info "مستعملو INDIM@J Partenaire"
    اكتب نفس العنوان **https://indimaj.tgr.gov.ma**: فهو يشمل أيضاً رابط الدخول إلى INDIM@J Partenaire (`https://indimaj.tgr.gov.ma/forms/frmservlet?config=INDJPAR`). لا داعي لإضافة عنوان ثانٍ.

<figure markdown="span">
  ![تمت إضافة الموقع إلى لائحة الاستثناءات](sites-exception-resultat.png){ width="560" }
  <figcaption>النتيجة المنتظرة: يظهر الرابط في لائحة المواقع المستثناة</figcaption>
</figure>

## الخطوة 12 — استيراد الشهادة إلى Java { #etape-12 }

<figure markdown="span">
  ![إدارة الشهادات](gerer-certificats.png){ width="760" }
  <figcaption>Java › Sécurité › Gérer les certificats</figcaption>
</figure>

1. في تبويب **Sécurité**، اضغط على **Gérer les certificats…**
2. في **Type de certificat**، اختر **Authentification du client**.
3. اضغط على **Importer**.
4. اختر ملف الشهادة **(.p12)** الذي حفظته في [الخطوة 7](../certificat/index.md#etape-7)، ثم اضغط على **Ouvrir**.
5. أدخل **كلمة مرور الحفظ** الخاصة بالشهادة.
6. إذا طُلبت كلمة مرور ثانية، اضغط على **OK** دون كتابة أي شيء.

<figure markdown="span">
  ![اختيار ملف الشهادة](importer-certificat.png){ width="760" }
  <figcaption>اختيار ملف الشهادة</figcaption>
</figure>

## الخطوة 13 — التحقق من إعدادات الأمان المتقدمة { #etape-13 }

<figure markdown="span">
  ![إعدادات الأمان المتقدمة](options-avancees.png){ width="560" }
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

1. اضغط على تبويب **Avancé**.
2. انزل إلى قسم **Paramètres de sécurité avancés**.
3. فعّل الخيارات أو ألغِ تفعيلها حسب الجدول أعلاه.
4. اضغط على **Appliquer**.

## الخطوة 14 — إيقاف تحديث Java { #etape-14 }

<figure markdown="span">
  ![تحديث Java](maj-java.png){ width="760" }
  <figcaption>Java › Mise à jour</figcaption>
</figure>

1. اضغط على تبويب **Mise à jour**.
2. أزل العلامة من خانة **Automatiser la recherche des mises à jour**.
3. اضغط على **OK** لإغلاق لوحة Java.

!!! warning "مهم"
    قد يؤدي التحديث التلقائي لـ Java إلى تعذّر الولوج إلى INDIM@J.
