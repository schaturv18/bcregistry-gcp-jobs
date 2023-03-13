# Copyright © 2023 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import psycopg2
import os
import time

def reindex_db():
    db_name = os.environ['DB_NAME']
    db_port = os.environ['DB_PORT']
    db_host = os.environ['DB_HOST']
    db_user = os.environ['DB_USER']

    # wait for port forward
    time.sleep(5)

    ret = 0
    try:
        connection = psycopg2.connect(user=db_user,
                                host=db_host,
                                port=db_port,
                                dbname=db_name)
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with connection.cursor() as cursor:
            cursor.execute("REINDEX DATABASE \"{0}\";".format(db_name))
    except Exception as error:
        print ("Exception:", error)
        print ("Exception TYPE:", type(error))
        ret = 1
    finally:
        if connection:
            connection.close()
        return ret


if __name__ == '__main__':
    reindex_db()