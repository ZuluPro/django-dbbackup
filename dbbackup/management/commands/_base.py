from optparse import make_option
from django.core.management.base import BaseCommand, LabelCommand
from django.utils import six

input = raw_input if six.PY2 else input  # @ReservedAssignment


class BaseDbBackupCommand(LabelCommand):
    option_list = BaseCommand.option_list + (
        make_option("--noinput", action='store_false', dest='interactive', default=True,
                    help='Tells Django to NOT prompt the user for input of any kind.'),
        make_option('-q', "--quiet", action='store_true', default=False,
                    help='Tells Django to NOT output other text than errors.')
    )

    verbosity = 1
    quiet = False

    def log(self, msg, level):
        """
        Print given message to stdout. Only print if verbosity level is
        greater than the given level.

        :param msg: Message to print
        :type msg: ``str``

        :param level: Message verbosity level
        :type level: ``int``
        """
        if not self.quiet and self.verbosity >= level:
            self.stdout.write(msg)

    def ask_yes_or_no(self, prompt, noinput=False, default=True):
        """
        Ask an input to user and convert string response into a boolean.
        Positive answer may be all string beginning by 'y'.

        :param prompt: Prompt used for ask question
        :type prompt: ``str``

        :param noinput: Use user's input or default response
        :type noinput: ``bool``

        :param default: Response to use if user's input is empty or
                        noinput option is used.
        :type default: ``bool``

        :returns: User's answer
        :rtype: ``bool``
        """
        answer = default if noinput else input(prompt)
        if not answer or noinput:
            return default
        return answer.strip().lower().startswith('y')
