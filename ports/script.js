var ports = ["Motherboard power", "CPU fan power", "CPU Socket or Slot", "PCI Slot", "PCI Express X1 Slot", "PCI Express X16 Slot", "Hard Drive Power", "Hard Drive Data (IDE)", "Hard Drive Data (SATA)", "VGA", "DVI", "HDMI", "PS2 Mouse", "PS2 Keyboard", "USB2", "USB3", "DisplayPort", "Thunderbolt", "Sound (7.1)", "SATA", "eSATA", "Ethernet", "Power", "Serial", "Parallel", "Games", "SVideo", "Optical Audio"]
var components = ["Motherboards power the SATA ports, USB powers, etc..", "CPU fan are powered by the motherboard. The Power Cable comes with the CPU fan.", "AMD and Intel have different type of sockets on the motherboard.", "Used for expansion cards and Peripherals. Used in parallel to split up work.", "Was designed to replace the old PCI slot.", "Has high transfer speeds (32gbps), is used for graphics cards, Optane drives, Wifi cards. and other expansion cards.", "Needs a cable cord, coming from the power supply. Hdd and Ssd takes very minimal energy (5-15w).", "Used for transferring storage, Sata is more popular nowadays.", "Connector for Storage on Computer, consists of three levels SATA 1, SATA 2, SATA 3 transferring 6gb of data per second.", "Outputs video on to Monitor/Panel. VGA is not usually used, as HDMI is its successor do to it being a better option. Consisted on IO shield of Motherboard and on Dedicated Graphics Cards.", "Outputs video on to Monitor/Panel. Consisted on IO shield of Motherboard and on Dedicated Graphics Cards. The DVI consists of two iterations. DVI-D, and DVI-I.", "Outputs video on to Monitor/Panel. Consisted on IO shield of Motherboard and on Dedicated Graphics Cards.", "Used on old computers, Port is extinct on nearly all computers. Used for mouse.", "Used on old computers, Port is extinct on nearly all computers. Used for  keyboard.", "Common interface found  on most computers now days, and are still used on modern computers. Interface is slower than USB 3 but costs cheaper and dosen’t not use as much power.", "USB 3 is a common interface used on today's computers only found on very modern computers. USB 3 is faster than USB 2 but is more costly and takes more energy.", "Used for high end Displays, due to the high data transfer rates.", "Used for outputting to monitor and use of eGPU.", "placeholder", "Used for external Hard drives and Ssds. Nowadays External storage uses usb.", "Connects devices to local network.", "Computer is powered using a PSU (Power supply). Wattage of PSU depends on the computer, ranging from 350 to 1500.", "Was used as a general interface used for almost everything, mouse, modems, and printers.", "Used for printers.", "Used back in the day, for controllers like joysticks and Midi input.", "In the days of 480i and 576i,  Svideo separated black and white to give  a better video quality though with some color inaccuracies.", "Used to send digital audio signals between devices."]
var images = ["http://s3.amazonaws.com/hs-wordpress/wp-content/uploads/2017/12/13130746/181_071.jpg", "http://www.buildcomputers.net/images/cpu-fan-power-connector-and-header.jpg", "https://assets.rockpapershotgun.com/images//2018/04/AM4-motherboard-header-620x320.jpg/RPSS/resize/760x-1/format/jpg/quality/90", "https://upload.wikimedia.org/wikipedia/commons/6/67/PCI_Slots_Digon3.JPG", "https://miningwholesale.eu/wp-content/uploads/2017/09/m.2_ngff_to_pci-e10-1.jpg", "https://cdn2.channelpro.co.uk/sites/channelpro/files/styles/article_main_wide_image/public/2016/04/pcix16.png?itok=mtfqWhL1", "https://images-na.ssl-images-amazon.com/images/I/61093cpc2BL._SL1280_.jpg", "https://cdn11.bigcommerce.com/s-qfzamxn9kz/images/stencil/original/products/125959/218738/hitachi-ic25n030atmr04-0-30gb-4-2k-ide-2-5-hard-disk-drive-hdd-5__74766.1534979451.jpg?c=2", "https://recoverit.wondershare.com/images/article/05/sata-hard-drive.jpg", "https://upload.wikimedia.org/wikipedia/commons/9/92/SVGA_port.jpg", "https://www.lifewire.com/thmb/MsObrF9kkmu4sahIkzgjkOAqtDQ=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/dvi-11299780447tnJ-5b0274196bf0690036ae84af.jpg", "http://publish.illinois.edu/mediacommonsblog/files/2016/02/pc-hdmi.png", "https://ae01.alicdn.com/kf/HTB16NCPOVXXXXc.XVXXq6xXFXXXz/500pcs-Green-PS2-Keyboard-Mouse-Jack-S-Terminal-Connector-Female-Socket-6-Core-PS2-6P-Terminal.jpg", "https://images-na.ssl-images-amazon.com/images/I/41FXJyOTRnL._SX466_.jpg", "https://azcd.harveynorman.com.au/media/catalog/product/a/o/ao-usbv24p-laser-usb-2-0-mini-4-port-hub.jpg", "https://www.maketecheasier.com/assets/uploads/2018/05/usb-3.1-gen-1-versus-gen-2-hero-800x400.jpg", "https://www.tradersalertes.com/wp-content/uploads/2017/12/cable_displayport_4m.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Thunderbolt_3_interface_USB-C_ports.jpg/220px-Thunderbolt_3_interface_USB-C_ports.jpg", "https://images-na.ssl-images-amazon.com/images/I/41nmWc4HyML._SX425_.jpg", "https://images-na.ssl-images-amazon.com/images/I/81M9eOK2aWL._SL1500_.jpg", "https://upload.wikimedia.org/wikipedia/commons/7/76/Esatap_port.JPG", "https://www.wikihow.com/images/5/58/Add-Ethernet-Ports-to-a-Router-Step-4.jpg", "https://www.jontrosky.com/images/pc_power.jpg", "https://upload.wikimedia.org/wikipedia/commons/e/ea/Serial_port.jpg", "https://upload.wikimedia.org/wikipedia/commons/f/fa/Parallel_computer_printer_port.jpg", "http://philipstorr.id.au/pcbook/images/joyone.gif", "https://www.lifewire.com/thmb/Ld4TFIZlKL03-GESE5aUrYrykaE=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/S-video-connection-57fa78fe3df78c690f76895b.jpg", "https://www.jsg-online.co.uk/ekmps/shops/glizdi/images/1m-digital-3.5mm-to-toslink-optical-digital-spdif-audio-cable-lead-979-p.jpg"]

index = 0;

function previous(){
    if(index > 0){
        index--;
    } else {
        index = 30;
    }

    document.getElementById("port").innerHTML = ports[index];
    document.getElementById("component").innerHTML = components[index];
    document.getElementById("image").src = images[index];
}

function next(){
    if(index  <30){
        index++;
    } else {
        index = 0;
    } 

    document.getElementById("port").innerHTML = ports[index];
    document.getElementById("component").innerHTML = components[index];
    document.getElementById("image").src = images[index];
}
