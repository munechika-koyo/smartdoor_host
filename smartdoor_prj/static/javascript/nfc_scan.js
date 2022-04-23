/*
scripts of scan NFC card IDm using SDK for NFC Web Client 1.1
This SDK is offered at 
https://www.sony.co.jp/Products/felica/business/products/sdk/ICS-DCWC1.html
*/

/* Define elements */
const scanModalEl = document.getElementById("scanModal");
const modalBody = document.querySelector(".modal-body");
const scanReload = document.getElementById("reload");
const idmInputField = document.getElementById("id_idm");

const loadingModalBody = [
    "<div class='d-flex align-items-center'>",
    "<div class='spinner-border m-3' role='status' aria-hidden='true'></div>",
    "<span>Please put your NFC card on reader.</span>",
    "</div>",
].join("");

/* Trigger loading NFC when the modal window shows up. */
scanModalEl.addEventListener("show.bs.modal", () => {
    scanReload.style.visibility = "hidden";
    modalBody.innerHTML = loadingModalBody;
    felica_card();
}, false);

/* Trigger loading NFC when the reload button is pushed. */
scanReload.addEventListener("click", () => {
    scanReload.style.visibility = "hidden";
    modalBody.innerHTML = loadingModalBody;
    felica_card();
}, false);



import { NFCPortLib, NFCPortError, Configuration, DetectionOption, CommunicationOption, TargetCard } from "https://cdn.felica-support.sony.biz/webclient/trial/NFCPortLib.js";

async function felica_card() {

    console.log("[Reading a FeliCa Card] Begin");

    let lib = null;

    try {
        /* create NFCPortLib object */
        lib = new NFCPortLib();

        /* init() */
        let config = new Configuration(500 /* ackTimeout */, 500 /* receiveTimeout */, true /* autoBaudRate*/, true /* autoDeviceSelect */);
        await lib.init(config);

        /* open() */
        await lib.open()

        console.log("deviceName : " + lib.deviceName);

        /* detectCard (FeliCa Card) */
        let detectOption = new DetectionOption(new Uint8Array([0xff, 0xff]), 0, true, false, null);

        let detected = false;
        let loopCount = 1;

        while (!detected) {
            await lib.detectCard("iso18092", detectOption)
                .then(ret => {
                    // Success Alert
                    modalBody.innerHTML = [
                        "<div class='alert alert-success d-flex align-items-center' role='alert'>",
                        "<svg class='bi flex-shrink-0 me-2' width='24' height='24'><use xlink:href='#check-circle-fill' /></svg>",
                        "<div>",
                        "Card is detected",
                        "</div>",
                    ].join("");

                    if (ret.systemCode == null) {
                        console.log("IDm : " + _array_tohexs(ret.idm) +
                            "\ntargetCardBaudRate : " + lib.targetCardBaudRate + "kbps");
                    } else {
                        console.log("IDm : " + _array_tohexs(ret.idm) +
                            "\nSystemCode : " + _array_tohexs(ret.systemCode) +
                            "\ntargetCardBaudRate : " + lib.targetCardBaudRate + "kbps");
                    }
                    // Fill in the IDm into input field 
                    idmInputField.value = _array_tohexs(ret.idm);

                    // Trigger detected flag
                    detected = true;

                    return ret;

                }, (error) => {
                    if (loopCount > 100) {
                        throw (error);
                    };
                });

            // loopCount increment
            loopCount++;

            // if modal window is close, terminate card detecting
            if (!scanModalEl.classList.contains("show")) {
                break;
            }
        }

        /* close() */
        await lib.close();
        lib = null;

    } catch (error) {
        console.log("Error errorType : " + error.errorType);
        console.log("      message : " + error.message);

        // Error Alert
        modalBody.innerHTML = [
            "<div class='alert alert-danger d-flex align-items-center' role='alert'>",
            "<svg class='bi flex-shrink-0 me-2' width='24' height='24'><use xlink:href='#exclamation-triangle-fill' /></svg>",
            "<div>",
            error.message + " (Error code : " + error.errorType + ")",
            "</div>",
        ].join("");


        if (lib != null) {
            await lib.close();
            lib = null;
        }

    }

    // show reload button
    scanReload.style.visibility = "visible";

    console.log("[Reading a FeliCa Card] End");
    return;
}

/* Local functions */
function _def_val(param, def) {
    return (param === undefined) ? def : param;
}

function _array_slice(array, offset, length) {
    let result;

    length = _def_val(length, array.length - offset);
    result = [];
    _array_copy(result, 0, array, offset, length);

    return result;
}

function _bytes2hexs(bytes, sep) {
    let str;

    sep = _def_val(sep, " ");

    return bytes.map(function (byte) {
        str = byte.toString(16);
        return byte < 0x10 ? "0" + str : str;
    }).join(sep).toUpperCase();
}

function _array_tohexs(array, offset, length) {
    let temp;

    offset = _def_val(offset, 0);
    length = _def_val(length, array.length - offset);

    temp = _array_slice(array, offset, length);
    return _bytes2hexs(temp, "");
}

function _array_copy(dest, dest_offset, src, src_offset, length) {
    let idx;

    src_offset = _def_val(src_offset, 0);
    length = _def_val(length, src.length);

    for (idx = 0; idx < length; idx++) {
        dest[dest_offset + idx] = src[src_offset + idx];
    }

    return dest;
}