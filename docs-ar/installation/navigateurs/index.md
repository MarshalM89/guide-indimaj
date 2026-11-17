# المرحلة 1 — تثبيت المتصفحات

## الخطوة 1 — تثبيت Firefox 52 ESR { #etape-1 }

[:material-download: Firefox Setup 52.0.1esr.exe](https://drive.google.com/drive/folders/1UZJvKztSVTUchLILuPxfFBg5bT1W3Tur?usp=drive_link){ .md-button .md-button--primary .dl target="_blank" }

1. حمّل الملف `Firefox Setup 52.0.1esr.exe` من [مجلد Google Drive الخاص بملفات التثبيت](https://drive.google.com/drive/folders/1UZJvKztSVTUchLILuPxfFBg5bT1W3Tur?usp=drive_link){ target="_blank" }.
2. انقر مرتين على الملف الذي تم تحميله.
3. اتبع مراحل التثبيت إلى النهاية.

!!! info "لماذا هذا الإصدار؟"
    Firefox 52 ESR هو آخر إصدار من Firefox يتوافق مع وحدة Java التي يستعملها INDIM@J. لا تثبّت إصداراً آخر.

## الخطوة 2 — إيقاف تحديث Firefox { #etape-2 }

<figure markdown="span">
  ![Firefox › Options › Avancé › Mises à jour](firefox-maj.png){ width="760" }
  <figcaption>Firefox › Options › Avancé › Mises à jour</figcaption>
</figure>

1. في Firefox، افتح القائمة **☰** ثم **Options**.
2. اضغط على **Avancé**، ثم على تبويب **Mises à jour**.
3. اختر **« Ne jamais vérifier les mises à jour »** (عدم التحقق من التحديثات أبداً).

!!! warning "مهم"
    التحديث التلقائي سيستبدل Firefox 52 ESR بإصدار غير متوافق، ولن يعود الولوج إلى INDIM@J ممكناً.

## الخطوة 3 — تثبيت Basilisk (32 bits) { #etape-3 }

<span class="badge-opt">اختياري</span>

[:material-download: basilisk-20261101213439.win32.installer.exe](https://dl.basilisk-browser.org/basilisk-20261101213439.win32.installer.exe){ .md-button .md-button--primary .dl }

1. حمّل Basilisk بنسخة 32 bits بواسطة الزر أعلاه.
2. انقر مرتين على الملف الذي تم تحميله.
3. اتبع مراحل التثبيت إلى النهاية.

!!! info "ما فائدة Basilisk؟"
    يتيح Basilisk (32 bits) استعمال INDIM@J كبديل عن Firefox 52 ESR. هذه الخطوة اختيارية.

!!! warning "Firefox يبقى ضرورياً للشهادة"
    لا يسمح Basilisk بتثبيت الشهادة. يجب إنشاء الشهادة وحفظها ([المرحلة 2](../certificat/index.md)) بواسطة Firefox 52 ESR.

!!! warning "ترتيب التثبيت"
    ثبّت Basilisk **قبل** Java ([المرحلة 3](../java/index.md)): لا تُضاف وحدة Java إلى المتصفح إلا إذا كان مثبتاً عند تثبيت Java. إذا كان Java مثبتاً من قبل، أعد تثبيته بعد Basilisk.
