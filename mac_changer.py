{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79171f0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "import optparse\n",
    "\n",
    "def get_arguments():\n",
    "    parser = optparse.OptionParser()\n",
    "    parser.add_option('-i','--interface', dest='interface',help='Interface to change its MAC address')\n",
    "    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')\n",
    "    (options, arguments) = get_arguments()\n",
    "    if not options.interface:\n",
    "        parser.error('Please specify an interface,use --help for more info.')\n",
    "    elif not options.new_mac:\n",
    "        parser.error('Please specify a MAC address,use --help for more info.')\n",
    "    return options\n",
    "        \n",
    "        \n",
    "\n",
    "def change_mac(interface, new_mac):\n",
    "    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)\n",
    "    subprocess.call(['ifconfig' ,interface, 'down'])\n",
    "    subprocess.call(['ifconfig' ,interface, 'hw', 'ether', new_mac])\n",
    "    subprocess.call(['ifconfig' ,interface, 'up'])\n",
    "    \n",
    "options = get_arguments()\n",
    "change_mac(options.interface, options.new_mac)\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
