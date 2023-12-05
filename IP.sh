#!/bin/bash
echo -e "\nEnter IP:\n"
read IPInput
if ! grep -q -E "export IP=\"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\"" ~/.zshrc; 
	then
	echo -e "export IP=\"$IPInput\"" >> ~/.zshrc
else	
	sed -i -E s/"export IP=\"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\""/"export IP=\"$IPInput\""/ ~/.zshrc
fi
echo -e "\n-------------------\n"
echo -e "\nIP exported as ${IP}\n\nExiting Program..."
